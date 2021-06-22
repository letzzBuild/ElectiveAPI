from roles.serializers import RolesSerializer
from django.shortcuts import render
from .models import Roles
from rest_framework.views import APIView
from .serializers import RolesSerializer
from rest_framework.response import Response

# Create your views here.
class AddRole(APIView):
    def post(self,request):
        serializer = RolesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

