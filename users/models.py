# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User


# class RegisterForm(UserCreationForm):
#     email = forms.EmailField()
#     # username = forms.EmailField(max_length=50, required=False)

#     class Meta:
#       model = User
#       fields = ["email", "password1", "password2"]


from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class RegisterForm(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=50)


    def __str__(self):
       return self.email
  
  
  # title = models.CharField(max_length=3, choices=TITLE_CHOICES)
  # birth_date = models.DateField(blank=True, null=True)
  # email = models.EmailField(max_length=70,blank=True)
 
 
 
  

# class Login(models.Model):
#   user_name = models.CharField(max_length=100)
#   password = models.CharField(max_length=100)
  
#   def greeting(self):
#     return self.user_name

# class RegisterForm(ModelForm):
#   class Meta:
#     model = Register
#     fields = ["first_name", "last_name", "username"]

# class LoginForm(ModelForm):
#   model = Login
#   fields = ["username", "password"]
  
  
  
# Create your models here.
# class Employee(models.Model):
#   first_name = models.CharField(max_length=100)
#   last_name = models.CharField(max_length=100)

# class Student(models.Model):
#   first_name = models.CharField(max_length=50)
#   last_name = models.CharField(max_length=50)
#   contact = models.IntegerField()
#   email = models.EmailField(max_length=254)
#   age = models.IntegerField()

# TITLE_CHOICES = {
#   "MR" : "Mr.",
#   "MRS": "Mrs.",
#   "MS": "Ms.",
# }