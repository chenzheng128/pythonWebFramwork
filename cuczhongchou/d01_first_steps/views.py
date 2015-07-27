# -*- coding: utf-8 -*-
from django.http.request import HttpRequest
from django.http.response import HttpResponse, Http404
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from django.template import RequestContext, loader

from django.shortcuts import get_object_or_404, render

from .models import Article, Question


"""
    Tutorial 03 file:///Users/chen/coding/documentations/django-docs-1.8-en/intro/tutorial03.html
"""

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ', '.join([p.question_text for p in latest_question_list])
    # #return HttpResponse(output)
    template = loader.get_template('d01_first_steps/index.html')
    context = RequestContext(request, {
        'latest_question_list': latest_question_list,
    })
    return HttpResponse(template.render(context))


def detail(request, question_id):
    #return HttpResponse("You're looking at question %s." % question_id)

    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404(u"找不到这个投票问题")
    question = get_object_or_404(Question, pk=question_id)

    return render(request, 'd01_first_steps/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


"""
#  Overview https://docs.djangoproject.com/en/1.8/intro/overview/
"""

def year_archive(request, year):
    a_list = Article.objects.filter(pub_date__year=year)
    context = {'year': year, 'article_list': a_list}
    return render(request, 'd01_first_steps/year_archive.html', context)

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
