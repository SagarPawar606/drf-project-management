from django.urls import path
from .views import (api_endpoints,
                    EmployeeView, 
                    ProjectView,
                    ProjectDetailView 
                    )

urlpatterns = [
    path('', api_endpoints, name='endpoints'),
    path('employee/', EmployeeView.as_view(), name='employee'),
    path('project/', ProjectView.as_view(), name='project'),
    path('project/<int:id>/', ProjectDetailView.as_view(), name='project-detail'),
]