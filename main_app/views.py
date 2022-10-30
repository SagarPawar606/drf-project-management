from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Employee

from .serializers import EmployeeSerializer, EmployeePostSerializer

# Create your views here.


@api_view(['GET'])
def api_endpoints(request):
    if request.method == 'GET':
        endpoints = {
            'get all employee' : 'employee/'
        }
        return Response(endpoints)

class Employees(APIView):
    def get(self, request):
        emp = Employee.objects.all()
        serializer = EmployeeSerializer(emp, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # def post(self, request):
    #     serializer = EmployeeSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        serializer = EmployeePostSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.data
            u = User(username=data.get("emp_name"), email=data.get("email"))
            u.save()
            e = Employee(user=u, position=data.get("position"), joining_date=data.get("joining_date"))
            e.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            


        
