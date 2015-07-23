# -*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.

from .models import Person, Article


#* 改进：显示filed（Person类）
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'age')


#* /admin/ 激活django 后台管理 Person 类， 进行持久化; 
admin.site.register(Person, PersonAdmin)


# 在列表显示 article 字段
class ArticleAdmin(admin.ModelAdmin):

	#后台 列表显示字段 
    list_display = ('title', 'contentShort', 'pub_date','update_time',)
    #* 改进：增加后台字段搜索
    search_fields = ('title', 'content',)

    #筛选功能
    list_filter = ('title', 'pub_date')

#* 激活 Article 类管理
admin.site.register(Article,ArticleAdmin)
