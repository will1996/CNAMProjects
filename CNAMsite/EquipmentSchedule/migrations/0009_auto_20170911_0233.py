# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-11 06:33
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('EquipmentSchedule', '0008_auto_20170911_0144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipmentslot',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 11, 6, 33, 18, 890000, tzinfo=utc), verbose_name='start time'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='hourallowance',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='hourtotal',
            field=models.FloatField(default=0),
        ),
    ]
