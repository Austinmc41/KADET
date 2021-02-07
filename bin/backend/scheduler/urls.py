from django.urls import path
from . import views

urlpatterns = [
    path('', views.criteria, name='scheduler-criteria'),
]
