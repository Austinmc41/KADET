from django.shortcuts import render

from rest_framework import viewsets
from .serializers import ScheduleSerializer
from .models import Schedule

class ScheduleView(viewsets.ModelViewSet):
    serializer_class = ScheduleSerializer
    queryset = Schedule.objects.all()
