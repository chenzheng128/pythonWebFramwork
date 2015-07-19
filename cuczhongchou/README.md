#python django 示范项目

使用django框架 完成一个众筹网站

用git管理学习代码(REAMDE文档保持在master中更新，其他代码保存在step0x【本章起始代码，便于开始此章实验】, step0x-done 【本章完成代码，便于查看本章效果】) (

为支持中文，所有的.py文件应在第一行中加入utf-8编码, 如下所示
```
# -*- coding: utf-8 -*-
```


##step01: 运行django的server代码
REF: Django 基本命令 http://www.ziqiangxuetang.com/django/django-basic.html

运行起来一个包含app示范代码，这些代码实际通过djangoadmin.py startproject cuczhongchou, python mange.py startapp learn, 两句命令就可以建立

```
git checkout master 

python manage.py runserver
```

##step02:
REF: Django 视图与网址 http://www.ziqiangxuetang.com/django/django-views-urls.html

这里完成的工作包括
* 新建一个应用(app), 名称叫 learn
* 把我们新定义的app加到settings.py中的INSTALL_APPS中
* 定义视图函数

```
git checkout step02  		#开始实验
git checkout step02-done  	#完成效果
```
