from .models import Ratings
from rest_framework import serializers
from faculty.models import Faculty
from electives.models import Electives

# Create your views here

class StudentHomePageSerializer(serializers.ModelSerializer):
    
    faculty_name = serializers.SerializerMethodField('get_faculty_name')
    
    elective_name = serializers.SerializerMethodField('get_elective_name')
    
    def get_faculty_name(self,rating_obj):
       elective_name = ""
       try:
           elective = Electives.objects.get(elective_id=rating_obj.elective_id.elective_id)
           elective_name  = elective.faculty_name
       except Exception as e:
           print(e)
           elective_name  = ""
       return elective_name 

    def get_elective_name(self,rating_obj):
       faculty_name = ""
       try:
           faculty = Faculty.objects.get(faculty_id=rating_obj.faculty_id.faculty_id)
           faculty_name = faculty.elective_name
       except Exception as e:
           print(e)
           faculty_name = ""
       return faculty_name   


   
    class Meta:
        model =  Ratings
        fields = ['stars','faculty_name','elective_name']

    
# class AverageFacultyRatingSerializer(serializers.Serializer):
#     stars_avg = serializers.FloatField(read_only=True) 