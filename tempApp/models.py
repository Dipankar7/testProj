from __future__ import unicode_literals

from django.db import models

# Create your models here.

class saveToDb(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    phoneNumber=models.PositiveIntegerField()
    checkIn=models.DateField(default="2011-10-11")
    
