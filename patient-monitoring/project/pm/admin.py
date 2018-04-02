from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class UserAdmin(UserAdmin):

    fieldsets = [
        ('User Info', {
            'fields': ['username', 'password', 'user_type', ]
            }),
        ('Personal info', {
            'fields': [
                'first_name',
                'last_name',
                'phone',
                'email',
                'date_of_birth',
                'gender',
                'blood_group',
            ]
            }),
        ('Permissions', {
            'fields': ['is_active', 'is_staff', 'is_superuser',]
            }),
    ]

admin.site.register(User, UserAdmin)
