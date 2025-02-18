from django.shortcuts import render

from django.utils.timezone import datetime


def home(request):
    return render(request, "myapp/home.html")


def about(request):
    return render(request, "myapp/about.html")


def contact(request):
    """
    This function handles the contact page request.

    Parameters:
    request (HttpRequest): The request object that contains metadata about the incoming HTTP request.

    Returns:
    HttpResponse: A response object that renders the "hello/contact.html" template.
    """
    return render(request, "myapp/contact.html")


def hello_there(request, name):
    print(request.build_absolute_uri())  # optional
    return render(
        request, "myapp/hello_there.html", {"name": name, "date": datetime.now()}
    )
