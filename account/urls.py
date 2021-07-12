from typing import ValuesView
from . import views
from django.urls import path, include


urlpatterns = [
    path('', views.home, name='home'),
    path('PatientDash/', views.dashboardPatient, name='PatientDash' ),
    path('DoctorDash/', views.dashboardDoctor, name='DoctorDash' ),
    path('login/', views.loginPage, name='login'),
    path('doctor/', views.registerDoctor, name='doctor'),
    path('patient/', views.registerPatient, name='patient'),
    path('logout/', views.logoutPage, name='logout'),
    path('choose/',views.Choose, name = 'choose'),
]