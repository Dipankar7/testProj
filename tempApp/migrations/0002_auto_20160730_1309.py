# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-30 13:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tempApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savetodb',
            name='checkIn',
            field=models.DateField(default='2011-10-11'),
        ),
    ]
