# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crowdfunding', '0002_auto_20150805_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='content',
            field=models.TextField(default='\u7a7a', verbose_name='\u8bf4\u660e'),
        ),
    ]
