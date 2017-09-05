# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class EquipmentSlot(models.Model):
    EQUIPMENT_LIST = (('PPMS', 'PPMS'), ('DYNACOOL', 'DynaCool'),
                                        ('IONMILL', 'ion mill'))
    start_time = models.DateTimeField('start time', default=timezone.now())
    slot_duration = models.DurationField('duration',
                                         default=datetime.timedelta(hours=1))
    equipment = models.CharField(max_length=20, choices=EQUIPMENT_LIST,
                                 default='PPMS')

    def __str__(self):
        return self.equipment

    def make_end_time(self):
        end_time = self.start_time + self.slot_duration
        return end_time

    def make_title(self):
        title = (self.equipment + ' is in use at ' + str(self.start_time) +
                 ' for ' + str(self.slot_duration))
        return title



class Meta:
    models.unique_together = (("equipment", "start_time"))
