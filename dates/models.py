# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import IntegrityError

from django.db import models

# Create your models here.

class date_for_scripting(models.Model):
    start_Date_Roll = models.DateField()
    end_Date_Roll = models.DateField()
    start_Date_Delta = models.DateField()
    end_Date_Delta = models.DateField()
    
    class Meta:
        db_table = "date_for_scripting"

class db_user_details(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    phone = models.IntegerField(default = 9876543210)

    class Meta:
        db_table = "user_details"


class AppConfig(models.Model):
	ry_start = models.DateField(null=True)
	ry_end = models.DateField(null=True)
	ryd_start = models.DateField(null=True)
	ryd_end = models.DateField(null=True)
	cr_start = models.DateField(null=True)
	cr_end = models.DateField(null=True)
	crd_start = models.DateField(null=True)
	crd_end = models.DateField(null=True)
	cr_quarter = models.CharField(max_length=50)
	pre_quarter = models.CharField(max_length=50)

	class Meta:
		db_table = "app_config"