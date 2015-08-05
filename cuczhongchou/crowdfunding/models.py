# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
# hahaha

# 我又增加了一些内容


class Project(models.Model):
    name = models.CharField(u"名称", max_length=200, default='')
    date_start = models.DateTimeField(u"开始时间")
    date_end = models.DateTimeField(u"结束时间")
    content = models.TextField(u"说明", default=u'空')
    amount_request = models.IntegerField(u"募款总额", default=0)
    amount_got = models.IntegerField(u"已获额度", default=0)
    def __unicode__(self):  # __unicode__ on Python 2
         return self.name + ' $' + str(self.amount_request)


class ProjectSupport(models.Model):
	pass

    