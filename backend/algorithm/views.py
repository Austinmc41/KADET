from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import StatusSerializer
from .models import AlgorithmStatus

from criteria.models import Criteria
from useraccess.models import SchedulerUser
from residentrequests.models import ResidentRequests

class StatusView(viewsets.ModelViewSet):
    serializer_class = StatusSerializer
    # queryset = AlgorithmStatus.objects.all()
    def get_queryset(self):
        for resident in SchedulerUser.objects.all():
            if resident.AccessLevel != 'not applicable':
                
        return AlgorithmStatus.objects.all()

        # AlgorithmStatus.objects.create
