# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-11-02 10:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('databases', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sample',
            name='id',
        ),
        migrations.AlterField(
            model_name='sample',
            name='user_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]