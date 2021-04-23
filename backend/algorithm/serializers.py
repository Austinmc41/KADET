from rest_framework import serializers 
from .models import AlgorithmStatus

class StatusSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = AlgorithmStatus 
        fields = ['id', 'Status']