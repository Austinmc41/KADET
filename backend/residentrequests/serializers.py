from rest_framework import serializers 
from .models import ResidentRequests

class RequestsSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = ResidentRequests 
        fields = '__all__'
        lookup_field = "email"