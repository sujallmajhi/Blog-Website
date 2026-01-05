from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


'''User registration form with username and password fields'''
class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=('username','password1','password2',)