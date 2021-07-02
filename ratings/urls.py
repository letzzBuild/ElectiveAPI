
from django.contrib import admin
from django.urls import path
from .views import StudentHomePageView

urlpatterns = [
    path('student/home',StudentHomePageView.as_view())
]
