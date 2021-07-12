from django.contrib.auth.forms import User
from django.contrib.auth.models import Group

from django.shortcuts import render, redirect
from .forms import DoctorForm, PatientForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Doctor, Patient
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    context = {}
    return render(request, 'account/home.html', context)



def loginPage(request):
    if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, "Username or password is incorrect")

    context = {}
    return render(request, 'account/login.html', context)

def logoutPage(request):
    logout(request)
    return redirect('login')

@login_required(login_url='home')
def dashboardPatient(request):
    namer = request.user
    try:
        form = Patient.objects.get(email__startswith=namer.email)
    except Patient.DoesNotExist:
        form = None    
    
        
    context = {'form': form}
    return render(request, 'account/dashboard.html', context)


@login_required(login_url='home')
def dashboardDoctor(request):
    namer = request.user

    try:
        form = Doctor.objects.get(email__startswith=namer.email)
        print(form.profile.url)
    except Doctor.DoesNotExist:
        form = None    
    
        
    context = {'form': form}
    return render(request, 'account/dashboard.html', context)
        

def Choose(request):
    context = {}
    return render(request, 'account/select.html', context)


def registerDoctor(request):
    
    if request.method == "POST":
        form = DoctorForm(request.POST)
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        
        if password1 == password2 and password1 != "":


            if form.is_valid():
                form.save()
            
            
            email = form.cleaned_data.get('email')

            

            user = User.objects.create_user(username=username, email=email, password = password1)                               
                                            
            user.save()

        

            messages.info(request,"An Account is Created Successfully")


            return redirect('DoctorDash')
        else:
            messages.info(request,"Password does not match, Try Again")
            return redirect('doctor')        
    else:
        form = DoctorForm()
    
    context = {'form':form}
    return render(request, 'account/register.html', context)


def registerPatient(request):
    
    if request.method == "POST":
        form = PatientForm(request.POST)

        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 == password2 and password1 != "":

                if form.is_valid():
                    form.save()
                
               
                email = form.cleaned_data.get('email')

                user = User.objects.create_user(username=username, email=email, password = password1)                               
                                                
                user.save()
                messages.info(request,"An Account is Created Successfully")


                return redirect('PatientDash')
        else:
            messages.info(request,"Password does not match, Try Again")
            return redirect('patient')        
    else:
        form = PatientForm()
    
    context = {'form':form}
    return render(request, 'account/register.html', context)
      
        
