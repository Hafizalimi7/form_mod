from django import forms  
from django.contrib.auth.models import User  
from django.contrib.auth.forms import UserCreationForm  
from django.core.exceptions import ValidationError  
from django.forms.fields import EmailField  
from django.forms.forms import Form  
from django.contrib import messages
from django.shortcuts import render, redirect

class register_form(UserCreationForm):
  first_name = forms.CharField(label='First Name', widget=forms.TextInput)
  last_name = forms.CharField(label='Last Name', widget=forms.TextInput)
  username = forms.CharField(label='Username', widget=forms.TextInput)
  email = forms.EmailField(label='Email')
  # date_of_birth = forms.DateInput(label='date_of_birth', widget=forms.)
  password1 = forms.CharField(label='password1', widget=forms.PasswordInput)
  password2 = forms.CharField(label='Comfirm Password', widget=forms.PasswordInput)
  class Meta():
    model = User
    fields = ('first_name', 'last_name', 'username', 'email','password1', 'password2')
  
  def handle_singUp(request):
    if request.method == "POST":
      f_name = request.POST['first_name']
      l_name = request.POST['last_name']
      userName = request.POST['username']
      email = request.POST['email']
      pwrd = request.POST['pasword']
      if User.objects.filter(username=userName).exists() or User.objects.filter(email=email).exists():
        myUser = User.objects.create_user(f_name, l_name, userName, email, pwrd)
        myUser.save()
        messages.success(request,"Your account has been created!")
      else:
        messages.error(request,"User already exists") # your error message
        return redirect(request.path)
            
    else:
        return render("404-Not found the page")

class login_form(forms.Form):
  username = forms.CharField(label='username', widget=forms.TextInput)
  password = forms.CharField(label='password', widget=forms.PasswordInput)
  
  def handle_login(request):
    if request.method == "POST":
      uname = request.POST["username"]
      pwd = request.POST["passowrd"]
      if User.objects.filter(username=uname).exists():
        myuser = User.objects.create_user(uname, pwd)
        myuser.save()
      else:
        messages.error(request,"User already exists")
  
  






