from rest_framework import serializers 
from .models import ResidentRequests

class RequestsSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = ResidentRequests 
        #fields = ['id', 'email', 'requestOne', 'requestTwo', 'requestThree']
        fields = '__all__'