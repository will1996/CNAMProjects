from django.conf.urls import url
from EquipmentSchedule import views as EquipmentSchedule_views
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout,
        {'next_page': '/EquipmentSchedule/logged_out/'}, name='logout'),
    url(r'^logged_out/$', views.logged_out, name="logged_out"),
    url(r'^index/$', views.index, name="index"),
    url(r'^Calendar/$', views.Calendar, name="Calendar"),
    url(r'^Calendar/create/$', views.create, name="create"),
    url(r'^signup/$', EquipmentSchedule_views.signup, name="signup"),
    url(r'^select_calendar/$', EquipmentSchedule_views.select_calendar,
        name="select_calendar"),
    url(r'^Calendar/view_event/$', views.view_event, name="view_event"),
]
