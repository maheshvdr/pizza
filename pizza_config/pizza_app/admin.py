# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Register your models here.

from django.contrib import admin

# Register your models here.
from pizza_app import models
admin.site.register(models.PizzaType)
admin.site.register(models.Pizza)
admin.site.register(models.Transactions)