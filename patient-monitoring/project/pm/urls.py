from django.contrib import admin
from django.urls import path,include
from pm import views

urlpatterns = [
    path('',views.home,name='home'),
    path('auth/patient/', views.auth_patient, name = 'auth_patient'),
    path('auth/staff/', views.auth_staff, name = 'auth_staff'),
]
