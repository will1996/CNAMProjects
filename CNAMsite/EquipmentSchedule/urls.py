from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^index/$', views.index, name="index"),
    url(r'^Calendar/$', views.Calendar, name="Calendar"),
    url(r'^Calendar/create/$', views.create, name="create")
]
