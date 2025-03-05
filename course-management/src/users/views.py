from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView
from django.contrib.auth import logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render


def login_view(request) -> ListView:
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect(
                reverse("index")
            )  # Replace 'index' with your dashboard URL nam
    else:
        form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form})


def custom_logout_view(request) -> ListView:
    """Logs out a user and redirects to the custom app's login page"""
    logout(request)
    return redirect(reverse("index"))
