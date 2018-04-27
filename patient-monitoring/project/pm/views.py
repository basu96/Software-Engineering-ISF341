from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import PatientLoginForm, StaffLoginForm, PatientCreateForm, AppointmentCreateForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .models import User, Appointment

@login_required(login_url = '/login/')
def home(request):
    return render(request, 'pm/home.html')

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
                    return redirect('/patient/view/' + user.username)
                else:
                    return HttpResponse('log in failed')
            else:
                return redirect('/login/')
    else:
        return redirect('/login/')

def auth_staff(request):
    form = StaffLoginForm(request.POST)

    if request.method == 'POST':
        if form.is_valid:
            username = form['username'].value()
            password = form['password'].value()

            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                return redirect('/home/')
            else:
                return redirect('/login/')
    else:
        return redirect('/login/')

def patient_view(request, uname):
    logged_in_user = request.user
    usr = get_object_or_404(User, username = uname)
    appointments = Appointment.objects.filter(patient=usr)
    context = {
        'user': usr,
        'appointments': appointments,
        'logged_in_user': logged_in_user,
    }
    if logged_in_user.user_type == 2:
        return render(request, 'pm/patient_view.html', context)
    else:
        return render(request, 'pm/patient_view_patient.html', context)

def patient_create(request):

    if request.method == 'GET':
        form = PatientCreateForm()
        context = {
            'form': form,
        }
        return render(request, 'pm/patient_create.html', context)

    elif request.method == 'POST':
        form = PatientCreateForm(request.POST)
        if form.is_valid:

            usr = User.objects.create(
                username = form['username'].value(),
                user_type = 1, # patient user type
                first_name = form['first_name'].value(),
                last_name = form['last_name'].value(),
                phone = form['phone'].value(),
                email = form['email'].value(),
                gender = form['gender'].value(),
                blood_group = form['blood_group'].value(),
                date_of_birth = form['date_of_birth'].value(),
            )
            usr.save()

        return HttpResponse('Form submitted')

def patient_remove(remove, uname):
    usr = get_object_or_404(User, username = uname)
    usr.delete()
    return HttpResponse('User removed')

def patient_edit(request, uname):
    usr = get_object_or_404(User, username = uname)

    if request.method == 'GET':
        values = {
            'username': usr.username,
            'first_name': usr.first_name,
            'last_name': usr.first_name,
            'phone': usr.phone,
            'email': usr.email,
            'gender': usr.gender,
            'blood_group': usr.blood_group,
            'date_of_birth': usr.date_of_birth,
        }

        form = PatientCreateForm(initial=values)
        context = {
            'form': form,
            'user': usr,
        }
        return render(request, 'pm/patient_edit.html', context)

    elif request.method == 'POST':
        form = PatientCreateForm(request.POST)
        if form.is_valid:

            usr.username = form['username'].value()
            usr.first_name = form['first_name'].value()
            usr.last_name = form['last_name'].value()
            usr.phone = form['phone'].value()
            usr.email = form['email'].value()
            usr.gender = form['gender'].value()
            usr.blood_group = form['blood_group'].value()

            dt = datetime.strptime(form['date_of_birth'].value(),'%Y-%m-%d').date()
            usr.date_of_birth = dt
            usr.save()

        return HttpResponse('Form submitted')

def test_view(request):
    return render(request, 'pm/testview.html')

@login_required(login_url='/login/')
def appointment_view_all(request):
    user = request.user
    appts = Appointment.objects.filter(doctor = user)
    context = {
        'appointments': appts,
    }
    return render(request, 'pm/appointments_all.html', context)

def appointment_view(request, id):
    logged_in_user = request.user
    appt = get_object_or_404(Appointment, pk = id)
    context = {
        'appt': appt,
        'logged_in_user': logged_in_user,
    }
    if(logged_in_user.user_type == 2):
        return render(request, 'pm/appointment_view.html', context)
    else:
        return render(request, 'pm/appointment_view_patient.html', context)

def appointment_create(request, uname = None):
    user = request.user
    if request.method == 'GET':
        if uname:
            patient = User.objects.get(username = uname)
            form = AppointmentCreateForm(initial = {'patient': patient, 'doctor': user})
        else:
            form = AppointmentCreateForm(initial = {'doctor': user})
        context = {
            'form': form,
        }
        return render(request, 'pm/appointment_create.html', context)

    elif request.method == 'POST':
        form = AppointmentCreateForm(request.POST)
        print(form.errors)
        if form.is_valid:
            form.save()
        return redirect('/home/')

def appointment_remove(request, id):
    return HttpResponse('pass')

def appointment_edit(request, id):
    return HttpResponse('pass')

def patient_view_all(request):
    patients = User.objects.filter(user_type = 1)
    context = {
        'patients': patients,
    }
    return render(request, 'pm/all_patients.html', context)

def logout_view(request):
    logout(request)
    return redirect('/login/')
