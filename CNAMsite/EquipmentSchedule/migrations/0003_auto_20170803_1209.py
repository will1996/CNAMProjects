# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-03 16:09
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('EquipmentSchedule', '0002_auto_20170803_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipmentslot',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 3, 16, 9, 0, 798000, tzinfo=utc), verbose_name='start time'),
        ),
    ]
