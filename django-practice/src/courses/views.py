from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from .models import Course


def index(request):
    return HttpResponse("Hello, world. You're at the courses index.")


class IndexView(generic.ListView):
    template_name = "courses/index.html"
    context_object_name = "latest_courses"

    def get_queryset(self, request):
        active_courses = Course.objects.filter(is_active=True)
        return render(request, "courses/index.html", {"courses": active_courses})


def courses_list(request):
    """Show active courses for anonymous users and enrolled courses for students"""
    if request.user.is_authenticated:
        student = request.user.student
        enrolled_courses = Course.objects.filter(enrollment__student=student)
        print(enrolled_courses)
        return render(request, "courses/index.html", {"courses": enrolled_courses})
    else:
        active_courses = Course.objects.filter(is_active=True)
        return render(request, "courses/index.html", {"courses": active_courses})
