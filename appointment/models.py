from django.db.models.deletion import CASCADE
from account.models import Patient
from django.db import models
from account.models import Patient, Doctor
# Create your models here.
from django.utils import timezone

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    speciality = models.CharField(max_length=50)
    date = models.CharField(max_length=20)
    is_patient_name = models.CharField(max_length=50)
    time = models.CharField(max_length=10)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return self.speciality


