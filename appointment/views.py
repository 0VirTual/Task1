from django.contrib import messages
from django.forms.utils import pretty_name

from django.shortcuts import redirect, render
from account.models import Doctor,Patient
from .models import Appointment
from django.forms import inlineformset_factory
from django.contrib import messages
from .forms import AppointmentForm


# Create your views here.
def check_doctor(request):
    doctor = Doctor.objects.all()

  

    context = {'doctor': doctor}
    return render(request, 'appointment/check_doctor.html', context)

def makeAppointment(request, pk):

    visitor = request.user
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        patient = Patient.objects.get(email=visitor.email)
        doctor = Doctor.objects.get(id=pk)
        if form.is_valid():
            form = AppointmentForm(request.POST)
            add = form.save(commit=False)
            add.patient = patient
            add.is_patient_name = patient.firstname+" "+patient.lastname
            add.date = request.POST.get('date')
            add.time = request.POST.get('time')
            add.doctor = doctor
            add.save()
            messages.info(request, "Appointment was created successfully")
            return redirect('account:home')
    else:
        form = AppointmentForm()


    

    context = {'form':form}
    return render(request, 'appointment/doctor_detail.html', context)

def checkAppointment(request):
    visitor = request.user
    finder = Doctor.objects.get(email=visitor.email)
    appointment = Appointment.objects.filter(doctor=finder)
    print(appointment)

    context = {'appointment':appointment}
    return render(request, 'appointment/appointment.html', context)