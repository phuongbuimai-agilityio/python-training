from django.shortcuts import render
from django.db.models import Q
from .models import Course


def courses_list(request):
    """Show active courses for anonymous users and enrolled courses for students"""
    search_query = request.GET.get("q", "")
    search_filter = Q(title__icontains=search_query) if search_query else Q()

    filter_option = request.GET.get("filter", "")

    if request.user.is_authenticated:
        if hasattr(request.user, "student"):
            courses = Course.objects.filter(
                Q(enrollment__student=request.user.student) & search_filter
            )
            # return render(request, "courses/index.html", {"courses": enrolled_courses})
        else:
            return render(
                request, "courses/error.html", {"message": "User is not a student."}
            )
    else:
        courses = Course.objects.filter(Q(is_active=True) & search_filter)
        # return render(request, "courses/index.html", {"courses": active_courses})

    # Sort the courses based on the filter option
    if filter_option == "created_asc":
        courses = courses.order_by("created")
    elif filter_option == "created_desc":
        courses = courses.order_by("-created")

    return render(
        request,
        "courses/index.html",
        {"courses": courses, "query": search_query, "filter_option": filter_option},
    )
