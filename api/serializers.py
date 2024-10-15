from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Employee

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["first_name","last_name","email","username","password"]

    def create(self, validated_data):
        return User.objects.create_user(**self.validated_data)


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields="__all__"