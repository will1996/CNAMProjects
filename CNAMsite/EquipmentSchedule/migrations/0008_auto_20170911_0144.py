# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-11 05:44
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('EquipmentSchedule', '0007_auto_20170910_2242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipmentslot',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 11, 5, 44, 28, 778000, tzinfo=utc), verbose_name='start time'),
        ),
    ]
