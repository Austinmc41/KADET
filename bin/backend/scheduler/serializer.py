from rest_framework import serializers 
from scheduler.models import Criteria
  
class CriteriaSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Criteria 
        fields = ['RotationType', 'TypeAmount']