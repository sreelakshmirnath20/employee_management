from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Employee(models.Model):

    name=models.CharField(unique=True,max_length=100)
    department=models.CharField(max_length=250)
    age=models.PositiveIntegerField()
    phone=models.PositiveIntegerField()
    salary=models.PositiveIntegerField()

    
    def __str__(self):
        return self.name
