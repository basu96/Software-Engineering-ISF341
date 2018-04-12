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
