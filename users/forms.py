from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Users

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = Users
        fields = ('username','email','phone','dob','gender')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = Users
        fields = ('username','email','phone','dob','gender')