from electives.models import ElectiveChoosenPriority
from django.urls import path
from .views import ElectivePriorityView, ElectivesForParticularSemester, ElectivesListView,ElectivesEnrolled,\
UploadElectiveInfo,FacultyAssignedToElective,\
ElectiveDetailsRetrieveUpdateAPIView,\
ElectiveSelectedListCreateAPIView,ElectiveDetailedReport


urlpatterns = [
    #for dropdown list of all electives
    path('allelectives/',ElectivesListView.as_view()),
    path('enrolled/electives/',ElectivesEnrolled.as_view()),
    path('upload/electiveinfo/',UploadElectiveInfo.as_view()),
    path('electivepriority/',ElectiveSelectedListCreateAPIView.as_view()),
    path('retriveupdate/electiveinfo/<int:pk>',ElectiveDetailsRetrieveUpdateAPIView.as_view()),
    path('assigned/faculty/',FacultyAssignedToElective.as_view()),
    path('elective/report/',ElectiveDetailedReport.as_view()),
    path('semelectives/student/<int:pk>',ElectivesForParticularSemester.as_view()),
    path('semelectives/student/<int:pk>',ElectivesForParticularSemester.as_view()),
    path('priority/',ElectivePriorityView.as_view())
]
