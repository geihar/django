from django.shortcuts import render
from .models import News


def main_page(request):

    data = {'news': News.objects.all()}
    return render(request, 'main_page/home.html', data)


def news(request):
    return render(request, 'main_page/news.html')

