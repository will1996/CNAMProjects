# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import EquipmentSlot
from .models import Profile

admin.site.register(EquipmentSlot)
admin.site.register(Profile)
