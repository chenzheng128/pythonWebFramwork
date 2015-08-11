# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('d01_first_steps', '0012_auto_20150806_1331'),
    ]

    operations = [
        migrations.CreateModel(
            name='D02Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='D02Membership',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_joined', models.DateField()),
                ('invite_reason', models.CharField(max_length=64)),
                ('group', models.ForeignKey(to='d01_first_steps.D02Group')),
            ],
        ),
        migrations.CreateModel(
            name='D02Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.AddField(
            model_name='d02membership',
            name='person',
            field=models.ForeignKey(to='d01_first_steps.D02Person'),
        ),
        migrations.AddField(
            model_name='d02group',
            name='members',
            field=models.ManyToManyField(to='d01_first_steps.D02Person', through='d01_first_steps.D02Membership'),
        ),
    ]
