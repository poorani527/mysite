from django.conf.urls import include, url
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^index$', views.index, name='index'),
    url(r'^search_form/', views.search_form, name = 'search_form'), #name - used to refer url.py action="{% url 'search_form' %}"
    url(r'^home/$', views.home),
    url(r'^datepicker/$', views.datepicker),
    url(r'^save/', views.save , name='save'),
    url(r'^show/', views.show , name='show'),
    url(r'^search_form1/(?P<id>[0-9]+)/$', views.search_form1, name = 'search_form1'),
    url(r'^delete/(?P<id>[0-9]+)/$', views.delete, name = 'delete'),
    url(r'^retreive/', views.retreive, name = 'retreive'),
    url(r'^app_config', views.app_config, name='app_config'),
    url(r'^rrr/', views.rrr, name = 'rrr'),

]