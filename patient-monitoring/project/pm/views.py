from django.shortcuts import render
from django.http import HttpResponse
from .forms import PatientLoginForm, StaffLoginForm

def home(request):
    return HttpResponse('test_response')

def login(request):
    patient_form = PatientLoginForm()
    staff_form = StaffLoginForm()
    context = {
        'patient_form': patient_form,
        'staff_form': staff_form,
    }
    return render(request,'login.html',context)
