from django.http import HttpResponse
from django.views import generic
from .models import Course


def index(request):
    return HttpResponse("Hello, world. You're at the courses index.")


class IndexView(generic.ListView):
    template_name = "courses/index.html"
    context_object_name = "latest_courses"

    def get_queryset(self):
        return Course.objects.filter(is_active=True)
