
from rest_framework import serializers 

from .models import Electives,ElectiveStudent,ElectiveDetails,ElectiveFaculty

class ElectiveListSerializer(serializers.ModelSerializer):
     
    class Meta:
      model = Electives 
      fields = '__all__'

class ElectiveInfoSerializer(serializers.ModelSerializer): 

   class Meta:
      model = ElectiveDetails
      fields =  '__all__' 


class FacultyAllocatedElective(serializers.ModelSerializer):
    class Meta:
      model = ElectiveFaculty
      fields = '__all__'





    