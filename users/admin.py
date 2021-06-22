from django.contrib import admin
from users.models import Users
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm,CustomUserCreationForm
from django import forms


class UserAdminConfig(UserAdmin):
    model = Users
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    search_fields = ('username','email')
    list_filter = ('username','is_active','is_staff' )
    list_display = ('username', 'is_active','is_staff' )
    fieldsets = (
        (None, {'fields': ('username','password','email','phone','dob','gender')}),
        ('Permissions', {'fields': ('is_active','is_staff')})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username','email','phone','dob','gender','password1', 'password2', 'is_active', 'is_staff')}
         ),
    )
    ordering = ('username','email')


admin.site.register(Users, UserAdminConfig)