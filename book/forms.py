from django import forms

from .models import Registration
from django.contrib.admin.widgets import AdminDateWidget

import datetime

class RegistrationForm(forms.ModelForm):

    class Meta:
        model = Registration
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter Name'}),
            'email':forms.EmailInput(attrs={'placeholder':'Enter Email ID'}),
            'checkIn':AdminDateWidget(attrs={'placeholder':'Check In Date'}),
            'checkOut':AdminDateWidget(attrs={'placeholder':'Check Out Date'}),

        }
        fields = ('name','email','phoneNumber','checkIn','checkOut','numberOfNights')



    def clean(self):
        date1=self.cleaned_data['checkIn']
        date2=self.cleaned_data['checkOut']
        if date1 < datetime.date.today():
            raise forms.ValidationError("The checkin date cannot be in the past!")
        elif date2 <= date1:
            raise forms.ValidationError("The check out date cannot be before checkin!")
        else:
            date1=self.cleaned_data['checkIn']
            date2=self.cleaned_data['checkOut']
            self.cleaned_data['noOfNights']=(date2-date1).days

        