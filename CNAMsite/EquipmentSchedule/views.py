# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from .models import EquipmentSlot
import datetime
from django.contrib.auth.models import User
from django.http import JsonResponse
from dateutil import parser


def index(request):
    return HttpResponseRedirect('url Calendar')


def Calendar(request):
    event_list = EquipmentSlot.objects.all()
    context = {'event_list': event_list}
    return render(request, 'EquipmentSchedule/Calendar.html', context)


def create(request):
    start = request.POST.get("start")
    end = request.POST.get("end")
    machine = request.POST.get("machine")
    start = parser.parse(start)
    length = datetime.timedelta(hours=float(end))
    EquipmentSlot.objects.get_or_create(start_time=start,
                                        slot_duration=length,
                                        equipment=machine)

    return JsonResponse()


def confirm():
    return locals()
