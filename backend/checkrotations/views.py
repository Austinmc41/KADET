from django.shortcuts import render

from rest_framework import viewsets
from .serializers import RotationStatusSerializer
from .models import RotationStatus

class RotationStatusView(viewsets.ModelViewSet):
    serializer_class = RotationStatusSerializer
    queryset = RotationStatus.objects.all()
