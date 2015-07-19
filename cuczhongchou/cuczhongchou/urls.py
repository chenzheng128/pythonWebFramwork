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

urlpatterns = [

 	# step02 Examples: 增加learn 应用中的 views.py 模块 中的 index(request) 方法
    url(r'^$', 'learn.views.index', name='home'),# Notice this line
    
    # step03 Examples: 从/add/?a=4&b=5 读取参数
    url(r'^add/$', 'learn.views.add', name='add'), # 注意修改了这一行

    # 采用 /add/3/4/ 这样的网址的方式
    url(r'^add/(\d+)/(\d+)/$', 'learn.views.add2', name='add2'),
    

    url(r'^admin/', include(admin.site.urls)),
]
