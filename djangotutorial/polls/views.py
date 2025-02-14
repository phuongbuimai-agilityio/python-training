from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Question


def index(request: HttpResponse) -> HttpResponse:
    """
    Render the index page with the latest poll questions.

    This view retrieves the 5 most recently published questions,
    ordered by their publication date in descending order, and
    renders them in the index template.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered index page with the latest questions.
    """
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {
        "latest_question_list": latest_question_list,
    }
    return render(request, "polls/index.html", context)


def detail(request: HttpResponse, question_id: int) -> HttpResponse:
    """
    Render the detail page for a specific poll question.

    This view retrieves a specific Question object by its primary key and
    renders the detail template with the question's details.

    Args:
        request (HttpRequest): The HTTP request object.
        question_id (int): The primary key of the Question to be displayed.

    Returns:
        HttpResponse: Rendered detail page with the specified question.

    Raises:
        Http404: If the Question with the given ID does not exist.
    """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})


def results(request: HttpResponse, question_id: int) -> HttpResponse:
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request: HttpResponse, question_id: int) -> HttpResponse:
    return HttpResponse("You're voting on question %s." % question_id)
