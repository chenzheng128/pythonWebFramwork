# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.core.urlresolvers import reverse

# Create your views here.
from django.http import HttpResponse

#常见异常import
from exceptions import ValueError
from django.utils.datastructures import MultiValueDictKeyError
 
#step02 默认首页
def index(request):

    return HttpResponse(u'''欢迎光临 传媒众筹网! 
    	<br>
    	<a href="./add/?a=4&b=5">add 处理参数方式1</a> 
    	<br>
    	<a href="./add/3/4/">add2 处理参数方式2</a> 

    	''')

#step03 处理add; 
# step03 Examples: 从/add/?a=4&b=5 读取参数
# urls.py url(r'^add/$', 'learn.views.add', name='add'), 
def add(request):
	try:
	    a = request.GET['a']
	    b = request.GET['b']
	    c = int(a)+int(b)
	    return HttpResponse("从/add/?a=4&b=5 读取参数:" + "a+b= " + str(c))
	
	#参数异常处理
	except ValueError as e:
		return HttpResponse("参数类型错误： 请输入数值"+ str(e) )
	except MultiValueDictKeyError as e:
		return HttpResponse("缺少参数: "+ str(e) )
	except Exception as e:
		print type(e)
		return HttpResponse("异常错误："+ str(e) )


# 采用 /add/3/4/ 这样的网址的方式
# urls.pyurl(r'^add/(\d+)/(\d+)/$', 'learn.views.add2', name='add2'),
def add2(request, a , b):
    c = int(a)+int(b)
    thisUrl=reverse('add2', args=(a,b));
    return HttpResponse(
    	u"""
    	<br>/add/3/4/ 网址的方式 读取参数: a+b= %d
    	<br> %s       网址的方式 读取参数: a+b= %d ; (网址由 reverse('add2', args=(a,b)) 函数生成)

    	""" % (c, thisUrl, c ))
