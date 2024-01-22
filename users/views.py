from django.shortcuts import render, redirect
from .forms import register_form
from .forms import login_form
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.hashers import make_password



def home(request):
  return render(request,'abc/home.html' )


def register_view(request):
    if request.method == "POST":
      form = register_form(request.POST)
      if form.is_valid():
        form.save()
        messages.success(request,f'YAY')
        return redirect('users:login')
    else:
        form = register_form()
    return render(request,"abc/register.html",{"form":form})
  
def login_view(request):
  if request.method == "POST":
    form = login_form(request.POST)
    if form.is_valid():
      username = form.cleaned_data['username']
      password = form.cleaned_data['password']
      user = authenticate(request, username=username, password=password)
      if user:
        login(request,user)
        return redirect('users:home')
  else:
    form = login_form()
  return render(request,"abc/login.html", {"form":form})


def user_logout_view(request):
  logout(request)
  return redirect('users:login')
