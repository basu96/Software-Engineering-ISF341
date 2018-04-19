from django.contrib import admin
from django.urls import path,include
from pm import views

urlpatterns = [
    path('',views.home,name='home'),
    path('auth/patient/', views.auth_patient, name = 'auth_patient'),
    path('auth/staff/', views.auth_staff, name = 'auth_staff'),

    path('patient/view/<str:uname>/', views.patient_view, name = 'patient_view'),
    path('patient/create/', views.patient_create, name = 'patient_create'),
    path('patient/remove/<str:uname>/', views.patient_remove, name = 'patient_remove'),
    path('patient/edit/<str:uname>/', views.patient_edit, name = 'patient_edit'),

]
