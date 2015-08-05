# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crowdfunding', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='amount_got',
            field=models.IntegerField(default=0, verbose_name='\u5df2\u83b7\u989d\u5ea6'),
        ),
        migrations.AlterField(
            model_name='project',
            name='amount_request',
            field=models.IntegerField(default=0, verbose_name='\u52df\u6b3e\u603b\u989d'),
        ),
        migrations.AlterField(
            model_name='project',
            name='content',
            field=models.TextField(default=b'', verbose_name='\u8bf4\u660e'),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(default=b'', max_length=200, verbose_name='\u540d\u79f0'),
        ),
    ]
