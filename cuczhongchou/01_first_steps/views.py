# -*- coding: utf-8 -*-
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

from doclearn.models import Article




### doclearn 官方 overview https://docs.djangoproject.com/en/1.8/intro/overview/
def year_archive(request, year):
    a_list = Article.objects.filter(pub_date__year=year)
    context = {'year': year, 'article_list': a_list}
    return render(request, 'doclearn/year_archive.html', context)

### 一个默认的snoop页面，便于调试
def snoop(request):
    # request = WSGIRequest()
    for key, value in request.POST:
        print key, value
    # raise ValueError("Got Some Error");
    return HttpResponse("snoop Response1" );
#
#

# Create your views here.
