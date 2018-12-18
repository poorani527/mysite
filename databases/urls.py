from django.conf.urls import include, url
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^showform$', views.showform, name='showform'),
     url(r'^db$', views.db, name='db'),


]