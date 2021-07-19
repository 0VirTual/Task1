from . import views
from django.urls import path, include



urlpatterns = [
    path('', views.check_doctor, name='check_doctor'),
    path('create/<int:pk>', views.makeAppointment, name='create'),
    path('list', views.checkAppointment, name='list')


    
]