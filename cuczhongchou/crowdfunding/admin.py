# -*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(ProjectSupport)

admin.site.register(Project)

