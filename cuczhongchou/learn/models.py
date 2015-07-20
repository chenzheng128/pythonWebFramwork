# -*- coding: utf-8 -*-
from django.db import models

"""
#创建一个person类，定义两个字段 姓名，年龄
"""
class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()


    """
    #定义toString，便于输出调试
    # 在Python3中使用 def __str__(self)
    """
    def __unicode__(self):
        return ("%s (%d)") % (self.name , self.age)

# Create your models here.
