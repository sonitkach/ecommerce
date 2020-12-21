from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
   name = forms.CharField(max_length=100, required=True) 
   surname = forms.CharField(max_length=100, required=True) 
   email = forms.EmailField(max_length=100, help_text='eg. youremail@gmail.com')

   class Meta:
       model=User
       fields = ('name', 'surname', 'username','password1', 'password2', 'email')