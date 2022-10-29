
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
project_status = [
        ('upcoming', 'Upcoming'),
        ('active', 'Active'),
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
    status = models.CharField(max_length=20, choices=project_status, default='upcoming')
    project_manager = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

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
    status = models.CharField(max_length=20, choices=project_status, default='upcoming')
    start_date = models.DateField()
    deadline_date = models.DateField()
    module_leader = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title
    
# project_module_list = [
#     (project.title, (
#             (module.id, str(module.title)) for module in Module.objects.filter(project=project)
#         ) 
#     ) for project in Project.objects.all() 
# ]

class ModuleTeam(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    member = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    role = models.CharField(max_length=255)

    def clean(self):
        '''will check if combination of project and module is valid or not'''
        if self.module.project != self.project:
            raise ValidationError('Please enter valid module, current module doesn\'t belong to this project')
        
    def __str__(self):
        return 'ModuleTeam - ' + self.module.title


