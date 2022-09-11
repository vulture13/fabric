from django.urls import path
from .views import my_fabric

urlpatterns = [
    path('', my_fabric)
]