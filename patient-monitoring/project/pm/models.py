from django.db import models
from django import forms
from django.contrib.auth.models import AbstractUser
from django.db.models import Q

class User(AbstractUser):

    USER_TYPE_CHOICES = (
        (1,'patient'),
        (2,'doctor'),
        (3,'staff'),
    )
    user_type = models.PositiveSmallIntegerField(null=True,choices = USER_TYPE_CHOICES)

    date_of_birth = models.DateField(auto_now=False, auto_now_add=False, null=True)
    phone = models.CharField(null=True, max_length=15)

    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    gender = models.CharField(
        max_length = 6,
        choices = GENDER_CHOICES,
        null = True,
        default = 'Other',
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
    blood_group = models.CharField(
        max_length = 5,
        choices = BLOOD_GROUP_CHOICES,
        null = True,
        default = 'Other',
    )

class Appointment(models.Model):
    # pass
    id = models.AutoField(primary_key = True)
    patient = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        limit_choices_to = Q(user_type = 1), # type 1 = patient
        related_name = 'patient',
        null = True,
    )
    doctor = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        limit_choices_to = Q(user_type = 2), # type 2 = doctor
        related_name = 'doctor',
        null = True,
    )
    date_time = models.DateTimeField(auto_now = True)
    blood_pressure = models.CharField(max_length = 10, null = True)
    breath_rate = models.PositiveSmallIntegerField(null = True) # units: bpm
    pulse_rate = models.PositiveSmallIntegerField(null = True) # units: bpm
    body_temperature = models.DecimalField(max_digits = 5, decimal_places = 2, null=True)
    report = models.TextField(max_length = 500, null = True)
    prescription = models.TextField(max_length = 500, null = True)
    prognosis = models.TextField(max_length = 500, null = True)
