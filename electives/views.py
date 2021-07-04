from typing import Generic
from .models import ElectiveFaculty,Electives
from rest_framework import generics
from .serializers import ElectiveListSerializer,FacultyAllocatedElective,ElectiveInfoSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import Electives,ElectiveStudent,ElectiveDetails
from rest_framework.response import Response
from rest_framework import status
import cloudinary.uploader as uploader
from rest_framework.parsers import MultiPartParser, JSONParser ,FormParser,FileUploadParser

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
      permission_classes = [IsAuthenticated]

      parser_classes = (
        MultiPartParser,
        JSONParser,
        FormParser,
        FileUploadParser
      )
      def post(self, request):
          serializer = ElectiveInfoSerializer(data=request.data)
          if serializer.is_valid():
              serializer.save()
              return Response("success",status=status.HTTP_200_OK)
          else:
               print("invalid serializer")
               return Response(serializer.errors,status=status.HTTP_500_INTERNAL_SERVER_ERROR)    
                      

class FacultyAssignedToElective(APIView):
    def get(self, request):
        try:
           queryset=ElectiveFaculty.objects.filter(faculty_id=request.data['faculty_id'])
           serializer = FacultyAllocatedElective(queryset)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        return Response(serializer.data,status=status.HTTP_200_OK)
        

class ElectiveDetailsRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = ElectiveDetails.objects.all()
    serializer_class = ElectiveInfoSerializer


