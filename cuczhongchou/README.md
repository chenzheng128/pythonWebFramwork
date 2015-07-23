#python django 示范项目

使用django框架 完成一个众筹网站所需的技术原型（prototype)

主要参考学堂在线课程， 并增加补充内容；在文档以及commit中标记为（补充内容）

用git管理学习代码(REAMDE文档保持在master中更新，其他代码保存在step0x【本章起始代码，便于开始此章实验】, step0x-done 【本章完成代码，便于查看本章效果】) (

注意：
* 这里代码的完成效果都是在learn app中完成的，而不是文章中的 xxxx app, 所以所有的 xxxx应修改为learn, 例如 learn.models 而不是 xxxx.models; 
* 所有代码中用到的home.html 都被修改为 step07.html
* 为支持中文，所有的.py文件应在第一行中加入utf-8编码, 如下所示
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

##step02: Django 视图与网址
REF:  http://www.ziqiangxuetang.com/django/django-views-urls.html

这里完成的工作包括
* 新建一个应用(app), 名称叫 learn
* 把我们新定义的app加到settings.py中的INSTALL_APPS中
* 定义视图函数

```
git checkout step02  		#开始实验
git checkout step02-done  	#完成效果
```
##step03: Django视图与网址进阶
REF: http://www.ziqiangxuetang.com/django/django-views-urls2.html

这里完成的工作包括
* 使用参数  在网页上读取参数，在 add add2 函数中做加减法处理
* 使用reverse()作反向解析(映射关系定义在urls.py中)。 将函数add2() 解析至真正的网站 add///;
* 增加参数异常处理（补充内容）


```
git checkout step03  		#开始实验
git checkout step03-done  	#完成效果
```

##step04: Django 模板


这里完成的工作包括
* 使用渲染模板
* 通用的部分模板，比如 导航，底部，访问统计代码


```
git checkout step04  		#开始实验
git checkout step04-done  	#完成效果
```

查看访问效果不再使用首页链接，而是使用 http://localhost:8000/step04b/ 这样的方式，举例链接可以查看 urls.py


##step05: Django 模型（数据库）
REF: http://www.ziqiangxuetang.com/django/django-models.html

注意：
* 自强学堂的链接不正确，所以本章的内容提前了，但是不影响，各章的内容是都是相对独立的。
* 这里代码的完成效果都是在learn app中完成的，而不是文章中的 people app, 所以所有的 people应修改为learn, 例如 learn.models 而不是 people.models; 

这里完成的工作包括
* 创建person持久化类  (models.py)
* 同步类与自动创建数据库person表格	
    - ./manage.py makemigrations (自动生成数据库映射文件 ./migrate/0001_person.py)
    - ./manage.py migrate (创建数据表)
* 在shell中完成person创建
* 在 /step05/ 模板中显示person list（补充内容）

```
git checkout step05  		#开始实验
git checkout step05-done  	#完成效果
```


##step06: Django 模板进阶
REF: http://www.ziqiangxuetang.com/django/django-template2.html

注意：
* 这里代码的完成效果都是在learn app中完成的，而不是文章中的 people app, 所以所有的 people应修改为learn, 例如 learn.models 而不是 people.models; 

这里完成的工作包括
* /step06a/ 显示一个变量(动态时间）信息在模板(step06a.html)中
* /step06b/ 显示List列表(for语法）信息在模板(step06b.html)中
* /step06c/ 显示Dict字典(for语法）信息在模板(step06c.html)中
* /step06d/ 条件判断显示(if 语法）    在模板(step06d.html)中

```
git checkout step06         #开始实验
git checkout step06-done    #完成效果
```


##step07: Django渲染json到模板
REF: http://www.ziqiangxuetang.com/django/django-json-templates.html

注意：
* 这里代码的完成效果都是在learn app中完成的，而不是文章中的 xxxx app, 所以所有的 xxxx应修改为learn, 例如 learn.models 而不是 xxxx.models; 
* 所有代码中用到的home.html 都被修改为 step07.html

这里完成的工作包括
* /step07/ python对象(List,Dict)转换为json在模板中加载

```
git checkout step07         #开始实验
git checkout step07-done    #完成效果
```

##暂时跳过的章节
* Django 自定义Field
* Django QuerySet API

##step08: Django 后台
REF: http://www.ziqiangxuetang.com/django/django-admin.html

这里完成的工作包括
* /admin/ 激活django 后台管理 Person 类， 进行持久化; 用户名:密码  admin:admin
* 激活 Article 类管理
    - ./manage.py makemigrations (自动生成数据库映射文件 ./migrate/0002_article.py)
    - ./manage.py migrate (创建数据表)
* 改进：显示filed（Person类）
* 改进：搜索
* 改进：筛选

```
git checkout step08         #开始实验
git checkout step08-done    #完成效果
```





