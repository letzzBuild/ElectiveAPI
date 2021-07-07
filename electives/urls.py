from django.urls import path
from .views import ElectivesListView,ElectivesEnrolled,\
UploadElectiveInfo,FacultyAssignedToElective,\
ElectiveDetailsRetrieveUpdateAPIView,\
ElectiveSelectedListCreateAPIView


urlpatterns = [
    #for dropdown list of all electives
    path('allelectives/',ElectivesListView.as_view()),
    path('enrolled/electives/',ElectivesEnrolled.as_view()),
    path('upload/electiveinfo/',UploadElectiveInfo.as_view()),
    path('electivepriority/',ElectiveSelectedListCreateAPIView.as_view()),
    path('retriveupdate/electiveinfo/<int:pk>',ElectiveDetailsRetrieveUpdateAPIView.as_view()),
    path('assigned/faculty/',FacultyAssignedToElective.as_view()),
    path('elective/report/<int:pk>',FacultyAssignedToElective.as_view()),
    
]
