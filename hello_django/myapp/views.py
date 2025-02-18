from django.shortcuts import render, redirect

from django.views.generic import ListView
from django.utils.timezone import datetime

from myapp.forms import LogMessageForm
from myapp.models import LogMessage


class HomeListView(ListView):
    """Renders the home page, with a list of all messages."""

    model = LogMessage

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context


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


def log_message(request):
    form = LogMessageForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return redirect("home")
    else:
        return render(request, "myapp/log_message.html", {"form": form})
