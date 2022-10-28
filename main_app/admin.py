from dataclasses import fields
from django.contrib import admin
from .models import Project, Employee, Module
# Register your models here.

class ModuleAdmin(admin.ModelAdmin):
    list_display = ('title', 'project')


admin.site.register(Project)
admin.site.register(Employee)
admin.site.register(Module, ModuleAdmin)


