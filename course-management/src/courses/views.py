from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Course
from django.http import HttpRequest, HttpResponse


def courses_list(request: HttpRequest) -> HttpResponse:
    """Render the courses list page.
    Args:
        request (HttpRequest): The HTTP request object.
    Returns:
        HttpResponse: The HTTP response object containing the rendered courses list page.
    """
    search_filter = get_search_filter(request)
    order_by = get_ordering(request)
    courses = get_courses(request, search_filter, order_by)
    if courses is None:
        return render(request, "courses/index.html", {})
    page_obj, paginator = paginate_courses(request, courses)

    return render(
        request,
        "courses/index.html",
        {
            "courses": page_obj,
            "query": request.GET.get("q", ""),
            "filter_option": request.GET.get("filter", "newest"),
            "paginator": paginator,
        },
    )


def get_search_filter(request: HttpRequest) -> Q:
    """Return the search filter based on the search query.

    Args:
        request (HttpRequest): The HTTP request object containing the search query.

    Returns:
        Q: The search filter to be used in the course query.
    """
    search_query = request.GET.get("q", "").strip()
    return Q(title__icontains=search_query) if search_query else Q()


def get_ordering(request: HttpRequest) -> str:
    """Return the ordering option based on the filter parameter.

    Args:
        request (HttpRequest): The HTTP request object containing the filter parameter.

    Returns:
        str: The ordering option to be used in the course query.
    """
    return "-created" if request.GET.get("filter") == "newest" else "created"


def get_courses(request: HttpRequest, search_filter: Q, order_by: str) -> Course:
    """Return the courses based on the search filter and ordering option.

    Args:
        request (HttpRequest): The HTTP request object containing the search filter and ordering option.
        search_filter (Q): The search filter to be used in the course query.
        order_by (str): The ordering option to be used in the course query.

    Returns:
        Course: The queryset of courses matching the search filter and ordering option.
    """
    if not request.user.is_authenticated:
        # Anonymous users see only active courses
        return Course.objects.filter(Q(is_active=True) & search_filter).order_by(
            order_by
        )

    if hasattr(request.user, "student"):
        # Authenticated students see their enrolled courses
        return Course.objects.filter(
            Q(enrollment__student=request.user.student) & search_filter
        ).order_by(order_by)

    # Non-student authenticated users return None
    return None


def paginate_courses(request: HttpRequest, courses: Course) -> tuple:
    """Paginate the courses based on the page size provided in the request.

    Args:
        request (HttpRequest): The HTTP request object containing the page size parameter.
        courses (Course): The queryset of courses to be paginated.

    Returns:
        tuple: A tuple containing the paginated courses and the paginator object.
    """
    page_size = request.GET.get("page_size", "5")
    try:
        page_size = max(1, int(page_size))
    except ValueError:
        page_size = 5

    paginator = Paginator(courses, page_size)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return page_obj, paginator
