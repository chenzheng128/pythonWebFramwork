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
    # 使用 include 和 namespace file:///Users/chen/coding/documentations/django-docs-1.8-en/intro/tutorial03.html
    url(r'^d01/', include('d01_first_steps.urls' , namespace="polls") ) ,

    ### learn 自强学社的参考代码
    url(r'^learn/', include('learn.urls' ) ),



    url(r'^admin/', include(admin.site.urls)),


]
