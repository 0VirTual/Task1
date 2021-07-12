from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms




from .models import Doctor, Patient

class DoctorForm(ModelForm):
    class Meta:
        model = Doctor
        fields = ('firstname', 'lastname', 'email', 'profile', 'address', 'zip' , 'city', 'state')

        
    
   

class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = ('firstname', 'lastname', 'email', 'profile', 'address', 'zip' , 'city', 'state')

        





# class CreateAddressForm(ModelForm):
#     class Meta:
#         model = Locate
#         fields = ['address', 'zip' , 'country']
#         widgets = {'country': CountrySelectWidget()}
        
       
