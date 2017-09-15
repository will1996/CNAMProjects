# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.http import HttpResponseRedirect, HttpResponse
from .models import EquipmentSlot
import datetime
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import JsonResponse
from dateutil import parser
from EquipmentSchedule.forms import SignUpForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('Calendar')
    else:
        form = SignUpForm()
    return render(request, 'EquipmentSchedule/signup.html', {'form': form})


def logged_out(request):

    return render(request, 'EquipmentSchedule/logged_out.html')


def index(request):
    return redirect('Calendar')


@login_required(login_url='login')
def Calendar(request):
    equipment = request.GET['E']
    event_list = EquipmentSlot.objects.filter(equipment=equipment)
    opperator = request.user.get_full_name()
    context = {'event_list': event_list, 'opperator': opperator, 'equipment': equipment}
    return render(request, 'EquipmentSchedule/Calendar.html', context)


def create(request):
    user = request.user
    opperator = request.POST['opperator']
    start = request.POST['start']
    start = parser.parse(start)
    machine = request.POST['machine']
    duration = request.POST['duration']
    length = datetime.timedelta(hours=float(duration))
    user.profile.hourallowance = user.profile.hourallowance-float(duration)
    user.profile.hourtotal = user.profile.hourtotal + float(duration)
    result = {'approved': True, 'NoHours': False, 'Overlap': False}
    if user.profile.hourallowance > float(duration):
        user.save()
        EquipmentSlot.objects.create(start_time=start,
                                     slot_duration=length,
                                     opperator=opperator,
                                     equipment=machine)

        return JsonResponse(result)
    else:
        result['approved'] = False
        result['NoHours'] = True
        return JsonResponse(result)


def select_calendar(request):
    list = ('PPMS', 'DynaCool', 'IonMill')
    context = {'list': list}
    return render(request, 'EquipmentSchedule/select_calendar.html', context)
