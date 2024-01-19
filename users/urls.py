from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("home/", views.home, name="users-home"),
    path('', views.register_view, name="register")
    # path('', views.sayhey,  name="base")

]
