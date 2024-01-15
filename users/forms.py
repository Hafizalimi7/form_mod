from django import forms  
from django.contrib.auth.models import User  
from django.contrib.auth.forms import UserCreationForm  
from django.core.exceptions import ValidationError  
from django.forms.fields import EmailField  
from django.forms.forms import Form  

class CustomUserCreationForm(UserCreationForm):
  username = forms.CharField(label='username', min_length=5, max_length=150)
  email = forms.EmailField(label='email')
  password1 = forms.CharField(label='password1', widget=forms.PasswordInput)
  password2 = forms.CharField(label='Comfirm Password', widget=forms.PasswordInput)