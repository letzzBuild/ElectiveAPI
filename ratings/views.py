from .models import Ratings
from .serializers import StudentHomePageSerializer
from rest_framework.views import APIView 
from .models import Ratings
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class StudentHomePageView(APIView):
    # permission_classes = [IsAuthenticated]    
    def get(self,request):
        electives = Ratings.objects.all()
        serializer = StudentHomePageSerializer(electives,many=True)
        return Response(serializer.data)








