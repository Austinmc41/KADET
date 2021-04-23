from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import StatusSerializer
from .models import AlgorithmStatus

class StatusView(viewsets.ModelViewSet):
    serializer_class = StatusSerializer
    queryset = AlgorithmStatus.objects.all()
