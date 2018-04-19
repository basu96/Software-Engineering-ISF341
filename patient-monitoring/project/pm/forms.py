from django import forms

import datetime

class PatientLoginForm(forms.Form):
    username = forms.CharField(label='Username',max_length=20)
    date_of_birth = forms.DateField(
        widget = forms.SelectDateWidget(years=range(1920, datetime.date.today().year))
    )


class StaffLoginForm(forms.Form):
    username = forms.CharField(label='Username',max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)


class PatientCreateForm(forms.Form):

    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    BLOOD_GROUP_CHOICES = (
        ('A+','A+'),
        ('A-','A-'),
        ('B+','B+'),
        ('B-','B-'),
        ('O+','O+'),
        ('O-','O-'),
        ('AB+','AB+'),
        ('AB-','AB-'),
        ('Other','Other'),
    )
    dob_range = range(1920, datetime.date.today().year)

    username = forms.CharField(label='Username', max_length=30)
    first_name = forms.CharField(label='First Name', max_length=30)
    last_name = forms.CharField(label='Last Name', max_length=30)
    phone = forms.CharField(label='Phone', max_length=15)
    email = forms.EmailField()
    gender = forms.ChoiceField(choices = GENDER_CHOICES)
    blood_group = forms.ChoiceField(choices = BLOOD_GROUP_CHOICES)
    date_of_birth = forms.DateField(
        widget = forms.SelectDateWidget(years=dob_range)
    )
