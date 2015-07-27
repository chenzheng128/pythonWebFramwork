# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import *

# Register your models here.

# Overview
admin.site.register(Article);
admin.site.register(Reporter);



"""
# 投票管理
# Tutorial polls
# admin.site.register(Question);
# admin.site.register(Choice);
"""

#class ChoiceInline(admin.StackedInline):   from
class ChoiceInline(admin.TabularInline):  # 比 StackedInline 更精简的模式

    model = Choice
    extra = 2  # 每次新增的数量


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'was_published_recently', 'checked') #在列表中显示栏目
    list_filter = ['pub_date', 'checked']  #筛选
    search_fields = ['question_text'] #文本搜索

    fieldsets = [  #定义表单组合, 不出现在这的字段,不会出现在表单中
        (None, {'fields': ['question_text', 'checked']}),

        ('填写组合', {'fields': ['pub_date', 'author'], 'classes': ['collapse']}),  # collapse 增加折叠效果
    ]
    inlines = [ChoiceInline]




admin.site.register(Question, QuestionAdmin)



class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish_date', 'user', 'status')  # 列表显示的字段
    search_fields = ('title',)  # 列表包含根据指定字段搜索
    list_filter = ('publish_date',)  # 右侧过滤选项

    # 分组表单
    fieldsets = (
        ('基本信息', {'fields': ('title', 'content', 'excerpt', 'publish_date', 'status', 'user', 'categories', 'tags')}),
        ('Meta Data', {'fields': ('alias', 'keywords', 'description')}),
    )



"""
#博客管理
"""

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
