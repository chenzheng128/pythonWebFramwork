# -*- coding: utf-8 -*-
import datetime

from django.db import models
from django.utils import timezone

"""
    所有的CharField都应该定义max_length, 便于除了SQLite之外的数据库支持
    定义Default值需要吗? 不一定 NULL (没填) 作为未填入的值 和 '' (填为空) 是不一样的.
"""

class Reporter(models.Model):
    full_name = models.CharField(max_length=70)

    def __unicode__(self):  # __unicode__ on Python 2
        return self.full_name


class Article(models.Model):
    pub_date = models.DateField()  # 日期型
    headline = models.CharField(max_length=200)
    content = models.TextField()  # TEXT文本型
    reporter = models.ForeignKey(Reporter)  # 创建外键

    def __unicode__(self):  # __unicode__ on Python 2
        return self.headline


"""
pools
Tutorial 01: https://docs.djangoproject.com/en/1.8/intro/tutorial01/
django 内置的filter已经很强大了

>>> from polls.models import Question, Choice

# Make sure our __str__() addition worked.
>>> Question.objects.all()
[<Question: What's up?>]

# Django provides a rich database lookup API that's entirely driven by
# keyword arguments.
>>> Question.objects.filter(id=1)
[<Question: What's up?>]
>>> Question.objects.filter(question_text__startswith='What')
[<Question: What's up?>]

# Get the question that was published this year.
>>> from django.utils import timezone
>>> current_year = timezone.now().year
>>> Question.objects.get(pub_date__year=current_year)
<Question: What's up?>

# Request an ID that doesn't exist, this will raise an exception.
>>> Question.objects.get(id=2)
Traceback (most recent call last):
    ...
DoesNotExist: Question matching query does not exist.

# Lookup by a primary key is the most common case, so Django provides a
# shortcut for primary-key exact lookups.
# The following is identical to Question.objects.get(id=1).
>>> Question.objects.get(pk=1)
<Question: What's up?>

# Make sure our custom method worked.
>>> q = Question.objects.get(pk=1)
>>> q.was_published_recently()
True

# Give the Question a couple of Choices. The create call constructs a new
# Choice object, does the INSERT statement, adds the choice to the set
# of available choices and returns the new Choice object. Django creates
# a set to hold the "other side" of a ForeignKey relation
# (e.g. a question's choice) which can be accessed via the API.
>>> q = Question.objects.get(pk=1)

# Display any choices from the related object set -- none so far.
>>> q.choice_set.all()
[]

# Create three choices.
>>> q.choice_set.create(choice_text='Not much', votes=0)
<Choice: Not much>
>>> q.choice_set.create(choice_text='The sky', votes=0)
<Choice: The sky>
>>> c = q.choice_set.create(choice_text='Just hacking again', votes=0)

# Choice objects have API access to their related Question objects.
>>> c.question
<Question: What's up?>

# And vice versa: Question objects get access to Choice objects.
>>> q.choice_set.all()
[<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]
>>> q.choice_set.count()
3

# The API automatically follows relationships as far as you need.
# Use double underscores to separate relationships.
# This works as many levels deep as you want; there's no limit.
# Find all Choices for any question whose pub_date is in this year
# (reusing the 'current_year' variable we created above).
>>> Choice.objects.filter(question__pub_date__year=current_year)
[<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]

# Let's delete one of the choices. Use delete() for that.
>>> c = q.choice_set.filter(choice_text__startswith='Just hacking')
>>> c.delete()

"""

class Question(models.Model):

    question_text = models.CharField(u"问题", max_length=200)

    pub_date = models.DateTimeField(u"发布日期")  # 日期与时间型

    author = models.CharField(u"发布人", max_length=50, default='')

    update_time = models.DateTimeField(u'更新时间', auto_now=True, null=True)

    checked = models.BooleanField(u'审核', default=False)

    class Meta:
        verbose_name = '投票问题'
        verbose_name_plural = '投票问题'

    # 增加自定义方法
    def was_published_recently(self):
        now = timezone.now()
        #return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True       #生成可爱的小图标
    was_published_recently.short_description = ' 是否最近更新'

    def __unicode__(self):  # __unicode__ on Python 2
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question)  # 创建外键
    choice_text = models.CharField(u"选项", max_length=200)
    sort = models.SmallIntegerField('排序', default=100)  # 排序
    votes = models.IntegerField(u"投票数", default=0)

    class Meta:
        verbose_name = '选项'
        verbose_name_plural = '选项'
        ordering = ['sort']

    def __unicode__(self):
        return self.choice_text

"""
# django 博客汉化方法 http://lishiguang.iteye.com/blog/1328986
"""

class Category(models.Model):
    """
    文章分类
    """
    title = models.CharField('名称', max_length=100)  # 分类名称
    alias = models.CharField('别名', max_length=100)  # 分类别名（用于 url 优化）
    sort = models.SmallIntegerField('排序', default=100)  # 排序

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = '分类'
        ordering = ['sort']

    def __unicode__(self):
        return self.title


class Tag(models.Model):
    """
    文章标签
    """
    tagname = models.CharField('标签名', max_length=60)  # 标签名
    post_ids = models.TextField(editable=False)  # 对应的文章 id 集合的序列

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = '标签'

    def __unicode__(self):
        return self.tagname


class Post(models.Model):
    """
    博客文章
    """
    # 文章发布状态
    CONTENT_STATUS_PUBLISHED = 1
    # 文章草稿箱状态
    CONTENT_STATUS_DRAFT = 2
    # 文章状态选项
    CONTENT_STATUS_CHOICES = (
        (CONTENT_STATUS_PUBLISHED, '发布'),
        (CONTENT_STATUS_DRAFT, '草稿箱'),
    )

    title = models.CharField('标题', max_length=100)  # 标题
    content = models.TextField('文章内容')  # 内容
    excerpt = models.TextField('摘要')  # 摘要
    publish_date = models.DateTimeField('发表时间')  # 发表时间
    status = models.IntegerField('状态',
                                 choices=CONTENT_STATUS_CHOICES,
                                 default=CONTENT_STATUS_PUBLISHED)  # 状态：1为正式发布，2为草稿箱
    comments_count = models.IntegerField(default=0, editable=False)  # 评论总数
    view_count = models.IntegerField(default=0, editable=False)  # 浏览总数

    alias = models.CharField('别名', max_length=100, blank=True)  # 别名（用于 url 优化）
    keywords = models.CharField('关键字', max_length=500, blank=True)  # 关键字
    description = models.TextField('描述', blank=True)  # 描述

    user = models.ForeignKey("auth.User",
                             verbose_name='作者',
                             related_name="%(class)ss")  # 作者
    categories = models.ManyToManyField(Category, blank=True,
                                        verbose_name='分类',
                                        related_name="posts")  # 分类

    tags = models.ManyToManyField(Tag, blank=True,
                                        verbose_name='标签',
                                        related_name="posts2")  # 标签

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'
        ordering = ['publish_date']

    def __unicode__(self):
        return self.title

    # Create your models here.
