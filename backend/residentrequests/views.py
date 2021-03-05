from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import RequestsSerializer
from .models import ResidentRequests

class RequestsView(viewsets.ModelViewSet):
    serializer_class = RequestsSerializer
    queryset = ResidentRequests.objects.all()