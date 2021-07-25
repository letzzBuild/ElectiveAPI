
from django.contrib import admin
from django.urls import path
from .views import StudentHomePageView,AverageFacultyRating,StudentRatings

urlpatterns = [
    path('student/home/<int:pk>/',StudentHomePageView.as_view()),
    path('averagerating/',AverageFacultyRating.as_view()),
    path('student/rating/',StudentRatings.as_view()),

]
