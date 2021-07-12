from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField, EmailField, IntegerField, TextField





# Create your models here.
class Doctor(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    profile = models.ImageField(default="user.png", null=True, blank=True, upload_to="images")
    email = models.CharField(max_length=50)
    zip = IntegerField()
    address = CharField(max_length=250)
    city = CharField(max_length=50, null=True)
    state = CharField(max_length=50, null=True)

    def __str__(self):
        return self.firstname
    
class Patient(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    profile = models.ImageField(default="user.png", null=True, blank=True, upload_to="images")
    email = models.CharField(max_length=50)
    zip = IntegerField()
    address = CharField(max_length=250)
    city = CharField(max_length=50, null=True)
    state = CharField(max_length=50, null=True)

    def __str__(self):
        return self.firstname
    



    

    
