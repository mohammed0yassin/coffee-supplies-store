from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from coffee_machines import views
from rest_framework.routers import DefaultRouter


urlpatterns = [     
    path('machines/', views.show_machines) 
    ]