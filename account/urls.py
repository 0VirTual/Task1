from typing import ValuesView
from . import views
from django.urls import path, include

app_name= 'account'


urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard' ),
    # path('DoctorDash/', views.dashboardDoctor, name='DoctorDash' ),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
    path('blog/', views.makeBlog, name='blog'),
    path('login/', views.loginPage, name='login'),
    path('doctor/', views.registerDoctor, name='doctor'),
    path('patient/', views.registerPatient, name='patient'),
    path('logout/', views.logoutPage, name='logout'),
    path('choose/',views.Choose, name = 'choose'),
]