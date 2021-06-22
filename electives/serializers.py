from django.db.models import fields
from rest_framework import serializers 
from .models import Electives

class ElectiveListSerializer(serializers.ModelSerializer):
    model = Electives
    fields = '__all__'
   
        



    