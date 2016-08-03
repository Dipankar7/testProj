from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Registration(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    phoneNumber=models.BigIntegerField()
    checkIn=models.DateField()
    checkOut=models.DateField()
    numberOfNights=models.IntegerField(default=0)
