# -*- coding: utf-8 -*-

"""cuczhongchou URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

import d01_first_steps.views

urlpatterns = [


    ### d01_first_steps 官方 overview https://docs.djangoproject.com/en/1.8/intro/overview/

    ### 使用 include 和 namespace file:///Users/chen/coding/documentations/django-docs-1.8-en/intro/tutorial03.html
    url(r'^d01/', include('d01_first_steps.urls' , namespace="polls") ) ,

    ### learn 自强学社

 	# step02 Examples: 增加learn 应用中的 views.py 模块 中的 simple(request) 方法
    url(r'^step02/$', 'learn.views.step02', name='step02'),# Notice this line
    
    # step03 Examples: 从/add/?a=4&b=5 读取参数
    url(r'^add/$', 'learn.views.add', name='add'), # 注意修改了这一行

    # 采用 /add/3/4/ 这样的网址的方式
    url(r'^add/(\d+)/(\d+)/$', 'learn.views.add2', name='add2'),

    # step04 Examples: 增加learn 应用中的 views.py 模块 中的 index(request) 方法
    url(r'^step04a/$', 'learn.views.step04a', name='learnStep04a'),# Notice this line

    url(r'^step04b/$', 'learn.views.step04b', name='learnStep04b'),# Notice this line

    url(r'^step05/$', 'learn.views.step05', name='learnStep05'),# Notice this line

    url(r'^step06a/$', 'learn.views.step06a', name=''),# Notice this line

    url(r'^step06b/$', 'learn.views.step06b', name=''),

    url(r'^step06c/$', 'learn.views.step06c', name=''),

    url(r'^step06d/$', 'learn.views.step06d', name=''),

    url(r'^step07/$', 'learn.views.step07', name=''),

    url(r'^step09/$', 'learn.views.step09', name=''),

    url(r'^admin/', include(admin.site.urls)),
]
