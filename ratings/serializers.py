from ratings.models import Ratings
from .models import Ratings
from rest_framework import serializers
from faculty.models import Faculty
from electives.models import Electives

# Create your views here

class StudentHomePageSerializer(serializers.ModelSerializer):
    
    faculty_name = serializers.SerializerMethodField('get_faculty_name')
    
    elective_name = serializers.SerializerMethodField('get_elective_name')
    
    def get_faculty_name(self,rating_obj):
       return rating_obj.faculty_id.faculty_name

    def get_elective_name(self,rating_obj):
       return rating_obj.elective_id.elective_name   


class StudentRatingSerializer(serializers.ModelSerializer):
   class Meta:
        model = Ratings
        fields = '__all__'
    