from django.db import models

# Create your models here.
from django.db import models

class Car(models.Model):
    company = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    year = models.DateField(max_length=100)
    kms_driven = models.IntegerField()
    fuel_type = models.CharField(max_length=100)

class LoginForm(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=8)
class signupForm(models.Model):
    username = models.CharField(max_length=20)
    email=models.CharField(max_length=50)
    password = models.CharField(max_length=8)
