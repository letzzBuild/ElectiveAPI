from typing import Generic
from .models import ElectiveFaculty,Electives
from rest_framework import generics
from .serializers import ElectiveListSerializer,FacultyAllocatedElective
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import Electives,ElectiveStudent,ElectiveDetails
from rest_framework.response import Response
from rest_framework import status
import cloudinary.uploader as uploader
from rest_framework.parsers import MultiPartParser, JSONParser ,FormParser

class ElectivesListView(generics.ListAPIView):
    queryset = Electives.objects.all()
    serializer_class = ElectiveListSerializer
    # permission_classes = [IsAuthenticated]

class ElectivesEnrolled(APIView):
    def post(self, request):
        student_id = request.data['user_id']
        
        try:
            elective_student = ElectiveStudent.objects.get(student_id=student_id)
            elective_id = elective_student.elective_id
            serializer = ElectiveListSerializer(elective_id)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            error = "something went wrong"
            return Response(error,status=status.HTTP_500_INTERNAL_SERVER_ERROR)    
        
class UploadElectiveInfo(APIView):
      parser_classes = (
        MultiPartParser,
        JSONParser,
        FormParser
      )


      def uploadFiles(self,file):
          result = uploader.upload_large(file,resource_type = "video")
          return result

      def post(self, request):
          
          return Response("hey")    

class FacultyAssignedToElective(APIView):
    def get(self, request):
        print(request.data)
        try:
           queryset=ElectiveFaculty.objects.filter(faculty_id=request.data['faculty_id'])
           serializer = FacultyAllocatedElective(queryset)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        return Response(serializer.data,status=status.HTTP_200_OK)
        
    