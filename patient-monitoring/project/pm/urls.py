from django.contrib import admin
from django.urls import path,include
from pm import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login',views.login_view,name='login'),
    path('auth/patient/', views.auth_patient, name = 'auth_patient'),
    path('auth/staff/', views.auth_staff, name = 'auth_staff'),
    path('testlink/', views.test_view, name = 'testlink'),
    path('home/', views.home, name = 'home'),
    path('logout/', views.logout_view, name = 'logout'),
    path('resources/', views.resources, name = 'resources'),

    path('patient/', views.patient_view_all, name = 'view_all_patients'),
    path('patient/view/<str:uname>/', views.patient_view, name = 'patient_view'),
    path('patient/create/', views.patient_create, name = 'patient_create'),
    path('patient/remove/<str:uname>/', views.patient_remove, name = 'patient_remove'),
    path('patient/edit/<str:uname>/', views.patient_edit, name = 'patient_edit'),

    path('appointment/', views.appointment_view_all, name = 'view_all_appointments'),
    path('appointment/view/<int:id>/', views.appointment_view, name = 'appointment_view'),
    path('appointment/create/<str:uname>/', views.appointment_create, name='appointment_create_named'),
    path('appointment/create/', views.appointment_create, name = 'appointment_create'),
    path('appointment/remove/<int:id>/', views.appointment_remove, name = 'appointment_remove'),
    path('appointment/edit/<int:id>/', views.appointment_edit, name = 'appointment_edit'),


]
