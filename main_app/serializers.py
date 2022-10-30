from rest_framework import serializers
from .models import Employee
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email']

        
# https://www.django-rest-framework.org/api-guide/serializers/#writable-nested-representations
class EmployeeSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Employee
        fields = '__all__'
    
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        print(validated_data)       # {'position': 'Backend developer', 'joining_date': datetime.date(2022, 10, 27)}
        print(user_data)            # OrderedDict([('username', 'newsagar'), ('email', 'newsagar@gmail.com')])
        user = User.objects.create(**user_data)
        employee = Employee.objects.create(user=user, **validated_data)
        return employee

