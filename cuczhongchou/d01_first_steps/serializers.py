# -*- coding: utf-8 -*-

from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import D01Article, D01Reporter, Question

"""
Rest Tutorial 1 serialzation
http://www.django-rest-framework.org/tutorial/1-serialization/
"""

from rest_framework import serializers
from .models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


"""
SnippetSerializerRaw 用 Serializer来序列化, 手工完成很多代码, 和设计Form表单很类似
"""
class SnippetSerializerRaw(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=90)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance

"""
SnippetSerializer 简化版本, 使用ModelSerializer , 类似于ModelForm, 很多信息从model中取出
查看实际生成的代码
>>> from snippets.serializers import SnippetSerializer
>>> serializer = SnippetSerializer()
>>> print(repr(serializer))
"""
class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')

"""
rest QuickStart
"""
class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = D01Article
        fields = ('headline', 'content', 'pub_date', 'reporter')

class ReporterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = D01Reporter
        fields = ('full_name', )


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
