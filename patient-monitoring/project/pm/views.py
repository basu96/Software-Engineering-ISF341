from django.shortcuts import render
from django.http import HttpResponse
from .forms import PatientLoginForm, StaffLoginForm
from django.contrib.auth import authenticate, login
from datetime import datetime
from .models import User

def home(request):
    return HttpResponse('test_response')

def login_view(request):
    patient_form = PatientLoginForm()
    staff_form = StaffLoginForm()
    context = {
        'patient_form': patient_form,
        'staff_form': staff_form,
    }
    return render(request,'login.html',context)

def auth_patient(request):
    if request.method == 'POST':
        form = PatientLoginForm(request.POST)
        if form.is_valid:
            username = form['username'].value()
            dob = form['date_of_birth'].value()
            print('latest',dob)

            user = User.objects.filter(username=username)
            if user is not None:
                user=user[0]
                if(str(user.date_of_birth) == str(dob)):
                    login(request, user)
                    return HttpResponse('logged in successfully')
                else:
                    return HttpResponse('log in failed')
            else:
                return HttpResponse('Invalid username')
    else:
        return HttpResponse('/auth/login')

def auth_staff(request):
    form = StaffLoginForm(request.POST)

    if request.method == 'POST':
        if form.is_valid:
            username = form['username'].value()
            password = form['password'].value()

            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                return HttpResponse('Login successful')
            else:
                return HttpResponse('Login failed')
    else:
        return HttpResponse('/auth/login')
