from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Article, Reporter, Question


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = ('headline', 'content', 'pub_date', 'reporter')

class ReporterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reporter
        fields = ('full_name', )


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
