from django.db import models

# Create your models here.
class Employee(models.Model):
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)

class Student(models.Model):
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  contact = models.IntegerField()
  email = models.EmailField(max_length=254)
  age = models.IntegerField()