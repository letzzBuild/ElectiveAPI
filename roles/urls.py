from django.contrib import admin
from django.urls import path,include
from .views import AddRole
urlpatterns = [
    path('addrole/',AddRole.as_view())
]