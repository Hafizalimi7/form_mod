from django.contrib import admin

# Register your models here.
from .models import RegisterForm, LoginForm


admin.site.register(RegisterForm)
admin.site.register(LoginForm)