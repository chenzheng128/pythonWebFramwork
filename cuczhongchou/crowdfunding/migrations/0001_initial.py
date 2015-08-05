# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name='\u540d\u79f0')),
                ('date_start', models.DateTimeField(verbose_name='\u5f00\u59cb\u65f6\u95f4')),
                ('date_end', models.DateTimeField(verbose_name='\u7ed3\u675f\u65f6\u95f4')),
                ('content', models.TextField(verbose_name='\u8bf4\u660e')),
                ('amount_request', models.IntegerField(verbose_name='\u52df\u6b3e\u603b\u989d')),
                ('amount_got', models.IntegerField(verbose_name='\u5df2\u83b7\u989d\u5ea6')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectSupport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
    ]
