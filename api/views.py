from django.shortcuts import render
from api.models import Employee
from api.serializers import UserSerializer,EmployeeSerializer
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication



# Create your views here.

class UserCreationView(ModelViewSet):
    serializer_class=UserSerializer
    queryset=User.objects.all()

class EmployeeModelViewSet(ModelViewSet):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]

    serializer_class=EmployeeSerializer
    queryset=Employee.objects.all()

    
        

