from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms




from .models import Appointment
from account.models import Doctor

class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        fields = ('speciality',)
    








