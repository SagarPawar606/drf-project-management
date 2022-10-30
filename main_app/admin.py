from dataclasses import fields
from django.contrib import admin
from .models import Project, Employee, Module, ModuleTeam
# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status')

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'position')

class ModuleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'project', 'priority')

class ModuleTeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'module', 'project', 'member')

admin.site.register(Project, ProjectAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Module, ModuleAdmin)
admin.site.register(ModuleTeam, ModuleTeamAdmin)


