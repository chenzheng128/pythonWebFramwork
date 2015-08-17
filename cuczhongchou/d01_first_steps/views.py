# -*- coding: utf-8 -*-
from django.http.request import HttpRequest
from django.http.response import HttpResponse, Http404, HttpResponseRedirect
from django.core.handlers.wsgi import WSGIRequest
from django.core.urlresolvers import reverse
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.utils import timezone

from .models import *


"""
django rest framework quickstart http://www.django-rest-framework.org/tutorial/quickstart/
"""

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .models import D01Article, D01Reporter
from .serializers import UserSerializer, GroupSerializer, ArticleSerializer, ReporterSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = D01Article.objects.all().order_by('-pub_date')
    serializer_class = ArticleSerializer


class ReporterViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = D01Reporter.objects.all()
    serializer_class = ReporterSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


"""
    Tutorial 03 file:///Users/chen/coding/documentations/django-docs-1.8-en/intro/tutorial03.html
"""

"""
    版本1: 手工实现
"""


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ', '.join([p.question_text for p in latest_question_list])
    # #return HttpResponse(output)
    template = loader.get_template('d01_first_steps/polls_index.html')
    context = RequestContext(request, {
        'latest_question_list': latest_question_list,
    })
    return HttpResponse(template.render(context))


def detail(request, question_id):
    # return HttpResponse("You're looking at question %s." % question_id)

    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404(u"找不到这个投票问题")

    # 上面代码的简化版本
    question = get_object_or_404(Question, pk=question_id)

    return render(request, 'd01_first_steps/polls_detail.html', {'question': question})


def results(request, question_id):
    # 简单模拟实现
    # response = "You're looking at the results of question %s."
    # return HttpResponse(response % question_id)

    # DAO操作
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'd01_first_steps/polls_results.html', {'question': question})


def vote(request, question_id):
    # 简单实现了此函数
    # return HttpResponse("You're voting on question %s." % question_id)

    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):  # 处理两个异常 KeyError 没有post choice, NotExist 找不到当前投票
        # Redisplay the question voting form.
        return render(request, 'd01_first_steps/polls_detail.html', {
            'question': p,
            'error_message': "请选择一个选项 ",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))


"""
版本2 : 使用通用模板 file:///Users/chen/coding/documentations/django-docs-1.8-en/intro/tutorial04.html#amend-views
"""


class IndexView(generic.ListView):
    template_name = 'd01_first_steps/polls_index.html'
    context_object_name = 'latest_question_list'

    # 原来的queryset ,没有logic判断
    # def get_queryset(self):
    #    """Return the last five published questions."""
    #    return Question.objects.order_by('-pub_date')[:5]

    # 新的query_set 增加时间判断
    def get_queryset(self):

        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'd01_first_steps/polls_detail.html'


    #过滤某些不希望显示的 Question
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'd01_first_steps/polls_results.html'


"""
#  Overview https://docs.djangoproject.com/en/1.8/intro/overview/
"""


def year_archive(request, year):
    a_list = D01Article.objects.filter(pub_date__year=year)
    context = {'year': year, 'article_list': a_list}
    return render(request, 'd01_first_steps/year_archive.html', context)


### 一个默认的snoop页面，便于调试
def snoop(request):
    # request = WSGIRequest()
    for key, value in request.POST:
        print key, value
    # raise ValueError("Got Some Error");
    return HttpResponse("snoop Response1");

#
#

# Create your views here.
