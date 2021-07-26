
from rest_framework import serializers 
from django.db.models import Avg
from .models import Electives,ElectiveStudent,ElectiveDetails,ElectiveFaculty,ElectiveSelected,ElectiveChoosenPriority, RecommanderQuestions
from ratings.models import Ratings

class ElectiveListSerializer(serializers.ModelSerializer):
     
    class Meta:
      model = Electives 
      fields = '__all__'

class ElectiveInfoSerializer(serializers.ModelSerializer):
   elective_name = serializers.SerializerMethodField('get_elective_name') 
   rating = serializers.SerializerMethodField('get_rating')

   def get_rating(self,ElectiveInfoObject):
      try:
          average_rating = Ratings.objects.filter(elective_id=ElectiveInfoObject.elective_id.elective_id).aggregate(Avg('stars'))
          return average_rating
      except Exception as e:
          print(e) 
          average_rating = 0
          return average_rating
   
   def get_elective_name(self,ElectiveInfoObject):
     try:
         elective = Electives.objects.get(elective_id=ElectiveInfoObject.elective_id.elective_id)
         elective_name = elective.elective_name
     except Exception as e:
         print(e) 
         elective_name = "not fetched"
     finally:
         return elective_name

   class Meta:
      model = ElectiveDetails
      fields =  '__all__' 


class FacultyAllocatedElective(serializers.ModelSerializer):
    elective_name = serializers.SerializerMethodField('get_elective_name')
    average_rating = serializers.SerializerMethodField('get_average_rating')
 

    def get_elective_name(self,obj):
        return obj.elective_id.elective_name
        
         
    def get_average_rating(self,obj):
      try:
          average_rating = Ratings.objects.filter(elective_id=obj.elective_id.elective_id).aggregate(Avg('stars'))
          return average_rating
      except Exception as e:
          print(e) 
          average_rating = 0
          return average_rating

    class Meta:
      model = ElectiveFaculty
      fields = '__all__'


class ElectiveSelectedSerializer(serializers.ModelSerializer):
   class Meta:
     model = ElectiveSelected
     fields = '__all__'

class ElectiveChoosenPrioritySerializer(serializers.ModelSerializer):
    class Meta:
        model = ElectiveChoosenPriority
        fields = '__all__'

class RecommanderQuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecommanderQuestions
        fields = '__all__'