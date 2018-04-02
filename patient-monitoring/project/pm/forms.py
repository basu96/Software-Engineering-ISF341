from django import forms

class PatientLoginForm(forms.Form):
    username = forms.CharField(label='Patient ID',max_length=20)
    date_of_birth = forms.DateField()

class StaffLoginForm(forms.Form):
    username = forms.CharField(label='Username',max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)
