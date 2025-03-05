from django.shortcuts import render
from django.db.models import Q
from .models import Course


def courses_list(request):
    """Show active courses for anonymous users and enrolled courses for students"""
    search_query = request.GET.get("q", "")
    search_filter = Q(title__icontains=search_query) if search_query else Q()

    filter_option = request.GET.get("filter", "newest")
    order_by = "-created" if filter_option == "newest" else "created"

    if request.user.is_authenticated:
        if hasattr(request.user, "student"):
            courses = Course.objects.filter(
                Q(enrollment__student=request.user.student) & search_filter
            ).order_by(order_by)
            # return render(request, "courses/index.html", {"courses": enrolled_courses})
        else:
            return render(
                request, "courses/error.html", {"message": "User is not a student."}
            )
    else:
        courses = Course.objects.filter(Q(is_active=True) & search_filter).order_by(
            order_by
        )
        # return render(request, "courses/index.html", {"courses": active_courses})

    # Sort the courses based on the filter option

    return render(
        request,
        "courses/index.html",
        {"courses": courses, "query": search_query, "filter_option": filter_option},
    )
