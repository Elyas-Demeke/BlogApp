from django.urls import path
from . import views

app_name = 'webapp'
urlpatterns = [
    path('', views.EmployeeList.as_view())
]
