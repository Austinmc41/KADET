from rest_framework import serializers 
from .models import Criteria

class CriteriaSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Criteria 
        fields = ['RotationType', 'MinResident', 'MaxResident']