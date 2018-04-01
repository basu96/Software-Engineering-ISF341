from django.db import models
from django import forms
from django.contrib.auth.models import AbstractUser

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
        max_length = 3,
        choices = BLOOD_GROUP_CHOICES,
        null = True,
        default = 'Other',
    )
