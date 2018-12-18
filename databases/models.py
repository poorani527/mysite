# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import IntegrityError

from django.db import models

# Create your models here.

class sample(models.Model):

   name = models.CharField(max_length = 50)
   user_id = models.IntegerField(primary_key=True)
   num1 = models.IntegerField()
   num2 = models.IntegerField()
   num3 = models.IntegerField()

   class Meta:
      db_table = "sample"