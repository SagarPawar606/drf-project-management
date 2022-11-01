from rest_framework import serializers
from .models import Employee, Project
from django.contrib.auth.models import User


"""
    Employee Serializers
"""
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email']

# https://www.django-rest-framework.org/api-guide/serializers/#writable-nested-representations
class EmployeeSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Employee
        fields = '__all__'      #   all the fields from UserSerializer also included here
    
    def create(self, validated_data):
        print(validated_data)       # {'user': OrderedDict([('username', 'newsagarnew'), ('email', 'newsagar@gmail.com')]), 'position': 'Backend developer', 'joining_date': datetime.date(2022, 10, 27)}
        user_data = validated_data.pop('user')
        print(user_data)            # OrderedDict([('username', 'newsagar'), ('email', 'newsagar@gmail.com')])
        user = User.objects.create(**user_data)
        employee = Employee.objects.create(user=user, **validated_data)
        return employee

"""
    Project Serializers
"""
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields =  '__all__'
       
