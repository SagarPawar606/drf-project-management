from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Employee, Project

from .serializers import EmployeeSerializer, ProjectSerializer


# Create your views here.

"""
    Employee views
"""
@api_view(['GET'])
def api_endpoints(request):
    if request.method == 'GET':
        endpoints = {
            'get all employee' : 'employee/'
        }
        return Response(endpoints)

class EmployeeView(APIView):
    def get(self, request):
        emp = Employee.objects.all()
        serializer = EmployeeSerializer(emp, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
"""
    Project views
"""
class ProjectView(APIView):
    def get(self,request):
        pro = Project.objects.all()
        serializer = ProjectSerializer(pro, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProjectDetailView(APIView):
    # grab and return particular model instance with provided id
    def get_object(self, id):
        pro = get_object_or_404(Project, id=id)
        return pro
        
    def get(self, request, id, format=None):
        pro = self.get_object(id)
        serializer = ProjectSerializer(pro)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # grab the model object and update it with request data
    def put(self, request, id, format=None):
        pro = self.get_object(id)
        serializer = ProjectSerializer(pro, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id, format=None):
        pro = self.get_object(id)
        pro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
  
        
