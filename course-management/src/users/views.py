from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import ListView
from django.contrib.auth import logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpRequest, HttpResponse


def login_view(request: HttpRequest) -> HttpResponse:
    """
    Handle user login view.

    If the user is already authenticated, they are redirected to the index page.
    If the request method is POST, it attempts to authenticate the user with the provided credentials.
    If the credentials are valid, the user is logged in and redirected to the index page.
    If the request method is GET, it renders the login form.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object with the rendered login form or a redirect to the index page.
    """
    if request.user.is_authenticated:
        return redirect(reverse("index"))

    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect(reverse("index"))
    else:
        form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form})


def custom_logout_view(request: HttpRequest) -> ListView:
    """Logs out a user and redirects to the custom app's login page"""
    logout(request)
    return redirect(reverse("index"))
