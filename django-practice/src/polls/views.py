from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.urls import reverse_lazy, reverse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class CustomLoginView(LoginView):
    template_name = "polls/login.html"
    success_url = reverse_lazy("index")  # Replace 'index' with your dashboard URL name
    redirect_authenticated_user = True


def custom_logout_view(request):
    """Logs out a user and redirects to the custom app's login page"""
    logout(request)
    return redirect(reverse("polls:login"))
