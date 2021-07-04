from .models import Ratings
from .serializers import StudentHomePageSerializer
from rest_framework.views import APIView 
from .models import Ratings
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.db.models import Avg

class StudentHomePageView(APIView):
    # permission_classes = [IsAuthenticated]    
    def get(self,request):
        electives = Ratings.objects.all()
        serializer = StudentHomePageSerializer(electives,many=True)
        return Response(serializer.data)

# Create your views here.
class AverageFacultyRating(APIView):
    def get(self, request,pk):
        average_rating = Ratings.objects.filter(faculty_id=pk).aggregate(Avg('stars'))
        print(average_rating)
        return Response(average_rating,status=status.HTTP_200_OK)







