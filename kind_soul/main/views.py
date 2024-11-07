from django.shortcuts import render
from .models import News


def index_view(request):
    return render(request, 'main/index.html')


def news_view(request):
    news_list = News.objects.all().order_by('-date')
    return render(request, 'main/news.html', {'news_list': news_list})
