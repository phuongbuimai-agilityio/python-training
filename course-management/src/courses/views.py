from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Course
from django.http import HttpRequest, HttpResponse


def courses_list(request: HttpRequest) -> HttpResponse:
    """
    Show active courses for anonymous users and enrolled courses for students.

    Args:
        request (HttpRequest): The HTTP request object containing GET parameters and user information.

    Returns:
        HttpResponse: The rendered HTML page displaying the list of courses.

    The function performs the following:
    - Retrieves the search query from the GET parameters and filters courses by title if provided.
    - Retrieves the filter option from the GET parameters and orders courses by creation date accordingly.
    - If the user is authenticated and is a student, it filters courses by the student's enrollment.
    - If the user is not authenticated, it filters active courses.
    - Paginates the courses list based on the page size provided in the GET parameters.
    - Renders the courses list in the "courses/index.html" template with pagination and search/filter options.
    """
    search_query = request.GET.get("q", "")
    search_filter = Q(title__icontains=search_query) if search_query else Q()

    filter_option = request.GET.get("filter", "newest")
    order_by = "-created" if filter_option == "newest" else "created"

    if request.user.is_authenticated:
        if hasattr(request.user, "student"):
            courses = Course.objects.filter(
                Q(enrollment__student=request.user.student) & search_filter
            ).order_by(order_by)
        else:
            return render(
                request, "courses/error.html", {"message": "User is not a student."}
            )
    else:
        courses = Course.objects.filter(Q(is_active=True) & search_filter).order_by(
            order_by
        )

    page_size = request.GET.get("page_size", "5")
    try:
        page_size = int(page_size)
    except ValueError:
        page_size = 5
    paginator = Paginator(courses, page_size)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "courses/index.html",
        {
            "courses": page_obj,
            "query": search_query,
            "filter_option": filter_option,
            "paginator": paginator,
        },
    )
