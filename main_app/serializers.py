from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class EmployeePostSerializer(serializers.Serializer):
    emp_name = serializers.CharField(max_length=255)
    email = serializers.EmailField()
    position = serializers.CharField(max_length=255)
    joining_date = serializers.DateField()