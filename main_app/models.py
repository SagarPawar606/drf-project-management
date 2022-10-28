from random import choices
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
project_status = [
        ('on_track', 'On track '),
        ('postponed', 'Postponed'),
        ('delayed', 'Delayed'),
        ('complted', 'Completed'), 
    ]


class Employee(models.Model):
    employee = models.OneToOneField(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=255)
    joining_date = models.DateField(blank=True)

    def __str__(self):
        return self.employee.username
    

class Project(models.Model):
    client = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    start_date = models.DateField()
    deadline_date = models.DateField()
    status = models.CharField(max_length=20, choices=project_status, default='on_track')
    project_manager = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title
    

class Module(models.Model):
    module_priority = [
        ('normal', 'Normal'),
        ('low', 'Low'),
        ('high', 'High'),
    ]
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    priority = models.CharField(max_length=10, choices=module_priority, default='normal')
    status = models.CharField(max_length=20, choices=project_status, default='in_progress')
    start_date = models.DateField()
    deadline_date = models.DateField()

    def __str__(self):
        return self.title



