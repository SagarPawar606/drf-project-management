from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_endpoints, name='endpoints'),
    path('employee/', views.Employees.as_view(), name='employee'),
]