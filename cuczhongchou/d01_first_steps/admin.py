# -*- coding: utf-8 -*-
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import *

# Register your models here.

"""
rest Tutorial snippets
"""
admin.site.register(Snippet)

"""
d02 admin
"""
admin.site.register(D02Album)
admin.site.register(D02Musician)

admin.site.register(D02Person)
admin.site.register(D02Group)
admin.site.register(D02Membership)

"""
d01 admin overview
"""

# Overview
admin.site.register(D01Article)
admin.site.register(D01Reporter)


"""
# d01 admin 投票管理
# Tutorial polls
# admin.site.register(Question);
# admin.site.register(Choice);
"""


class ChoiceInline(admin.TabularInline):  # 比 StackedInline 更精简的模式
    # class ChoiceInline(admin.StackedInline):   from

    model = Choice
    extra = 2  # 每次新增的数量


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date',
                    'was_published_recently', 'checked')  # 在列表中显示栏目
    list_filter = ['pub_date', 'checked']  # 筛选
    search_fields = ['question_text']  # 文本搜索

    fieldsets = [  # 定义表单组合, 不出现在这的字段,不会出现在表单中
        (None, {'fields': ['question_text', 'checked']}),

        ('填写组合', {'fields': ['pub_date', 'author'], 'classes': ['collapse']}),  # collapse 增加折叠效果
    ]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)

class PostAdmin(ImportExportModelAdmin):
    list_display = ('title', 'checked', 'publish_date', 'user', 'status', )  # 列表显示的字段
    search_fields = ('title',)  # 列表包含根据指定字段搜索
    list_filter = ('publish_date',)  # 右侧过滤选项

    # 分组表单
    fieldsets = (
        ('基本信息', {'fields': ('title', 'checked', 'content', 'excerpt', 'publish_date', 'status', 'user', 'categories', 'tags')}),
        ('Meta Data', {'fields': ('alias', 'keywords', 'description', )}),
    )

class PostAdminCheck(admin.ModelAdmin):
    list_display = ('title', 'checked',)  # 列表显示的字段
    search_fields = ('title',)  # 列表包含根据指定字段搜索
    list_filter = ('publish_date',)  # 右侧过滤选项

    # 分组表单
    fieldsets = (
        ('基本信息', {'fields': ('title', 'checked', 'content', 'excerpt', 'publish_date', 'status', 'user', 'categories', 'tags')}),
        ('Meta Data', {'fields': ('alias', 'keywords', 'description', )}),
    )

"""
#博客管理
"""

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
