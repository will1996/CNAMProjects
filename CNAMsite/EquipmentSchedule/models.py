# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from django.db.models.signals import post_save
from django.dispatch import receiver


@python_2_unicode_compatible
class EquipmentSlot(models.Model):
    EQUIPMENT_LIST = (('PPMS', 'PPMS'), ('DYNACOOL', 'DynaCool'),
                                        ('IONMILL', 'ion mill'))
    start_time = models.DateTimeField('start time', default=timezone.now())
    slot_duration = models.DurationField('duration',
                                         default=datetime.timedelta(hours=1))
    equipment = models.CharField(max_length=20, choices=EQUIPMENT_LIST,
                                 default='PPMS')
    opperator = models.CharField(max_length=128, default='anonymous')

    def __str__(self):
        label = (u'Equipment: '+str(self.equipment)+u'        User: '+str(self.opperator)+u'         Start Time: '+str(self.start_time)+u'        Duration: '+str(self.slot_duration))
        return label

    def make_end_time(self):
        end_time = self.start_time + self.slot_duration
        return end_time

    def make_title(self):
        title = (self.equipment + ' is in use at ' + str(self.start_time) + '  by  '
                 + self.opperator + ' for ' + str(self.slot_duration))
        return title


@python_2_unicode_compatible
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    hourallowance = models.FloatField(default=10)
    hourtotal = models.FloatField(default=0)

    def __str__(self):
        info = (u'user:'+str(self.user)+u'   hours used:'+str(self.hourtotal)+u'   hours remaining:'+str(self.hourallowance))
        return info

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Meta:
    models.unique_together = (("equipment", "start_time"))
