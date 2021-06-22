
from rest_framework import serializers
from .models import Users
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from students.models import Students
from faculty.models import Faculty

class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
            password = validated_data.pop('password')
            user = super().create(validated_data)
            user.set_password(password)
            user.save()
            return user

    class Meta:
        model = Users
        fields = '__all__'


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):


    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        # Add extra responses here
        data['username'] = self.user.username
        data['email'] = self.user.email
        data['phone'] = self.user.phone
        data['dob'] = self.user.dob
        data['gender'] = self.user.gender
        try:
            Students.objects.get(user_id=self.user.user_id)
            data['role'] = 'student'
            return data
        except Exception as e:
            print(e)     
        try:
            Faculty.objects.get(user_id=self.user.user_id)
            data['role'] = 'faculty'
            return data
        except:
            data['role'] = 'none'
            
        return data 

                
                     


             




