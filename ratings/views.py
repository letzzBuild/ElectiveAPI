from faculty.models import Faculty
from electives.models import ElectiveFaculty, ElectiveSemester
from students.models import Students
from .models import Ratings
from .serializers import StudentHomePageSerializer, StudentRatingSerializer
from rest_framework.views import APIView 
from .models import Ratings
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.db.models import Avg

class StudentHomePageView(APIView):
    # permission_classes = [IsAuthenticated]    
    def get(self,request,pk):
        result = []
        elective_object = {}
        student=Students.objects.get(student_id=pk)
        semester_id = student.semester_id
        print(semester_id.semester_id)
        elective_semester=ElectiveSemester.objects.filter(semester_id=semester_id.semester_id)
        print(elective_semester)
        for elective in elective_semester:
            elective_object['elective_name'] = elective.elective_id.elective_name
            average_rating = Ratings.objects.filter(elective_id=elective.elective_id.elective_id).aggregate(Avg('stars'))
            elective_object['ratings'] = average_rating['stars__avg']
            print(elective.elective_id.elective_id)
            faculties = ElectiveFaculty.objects.get(elective_id=elective.elective_id.elective_id)
            elective_object['faculty_name'] = faculties.faculty_id.faculty_name
            result.append(elective_object)
            print(elective_object)
            elective_object = {}
        return Response(result)

# Create your views here.
class AverageFacultyRating(APIView):
    def get(self, request,pk):
        average_rating = Ratings.objects.filter(faculty_id=pk).aggregate(Avg('stars'))
        print(average_rating)
        return Response(average_rating,status=status.HTTP_200_OK)

#write updating logic
class StudentRatings(APIView):
    def post(self, request):
        
        data = request.data
        try:
            elective_faculty=ElectiveFaculty.objects.get(elective_id=request.data['elective_id'])
            faculty_id=elective_faculty.faculty_id.faculty_id
            data['faculty_id']=faculty_id
            serializer = StudentRatingSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response("ratings has been recorded successfully",status=status.HTTP_200_OK)    
        except Exception as e:
            print(e) 
            return Response("failed to to add ratings",status=status.HTTP_500_INTERNAL_SERVER_ERROR)   
        












