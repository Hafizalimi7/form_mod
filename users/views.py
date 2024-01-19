from django.shortcuts import render, redirect
from .forms import register_form
from django.contrib import messages
from django.contrib.auth.models import User




# Create your views here.
# def register(response):
#     if response.method == "POST":
#       form = RegisterForm(response.POST)
#       if form.is_valid():
#         form.save()
#         return redirect("/home")
#     else:
#       form = RegisterForm()
#     return render(response, "abc/register.html", {"form":form})

def home(request):
  return render(request,'templates/home.html' )


def register_view(request):
    if request.method == "POST":
      form = register_form(request.POST)
      if form.is_valid():
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        messages.success(request,f'your account has been created successfully! you are able to login')
        return "Heyyy"
    else:
        form = register_form()
    return render(request,"abc/register.html",{"form":form})
  

# if not request.user.is_authenticated:
#         if request.method == 'POST':
#             form = register_form(request.POST)
#             if form.is_valid():
#                 username = models.cleaned_data['username']
#                 password = models.cleaned_data['password']
#                 user = authenticate(username=username , password=password)
#                 if user is not None:
#                     login(request , user)
#                     messages.success(request,'logged in Successfully !!')
#                     return redirect('dashbord')
#                 else:
#                     form = LoginForm() 
#         else:
#             return HttpResponseRedirect('dashbord')
#     else:
#         form = LoginForm()
#     return render(request,'login.html',{'form':form})
  
