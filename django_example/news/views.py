from django.shortcuts import render

from .models import Article


def year_archive(request, year):
    a_list = Article.objects.filter(pub_date__year=year)
    context = {"article_list": a_list, "year": year}
    return render(request, "news/year_archive.html", context)
