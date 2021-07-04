
from django.contrib import admin
from django.urls import path
from .views import StudentHomePageView,AverageFacultyRating

urlpatterns = [
    path('student/home',StudentHomePageView.as_view()),
    path('averagerating/<int:pk>',AverageFacultyRating.as_view()),

]
