from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import StatusSerializer
from .models import AlgorithmStatus

import math
from datetime import date
from criteria.models import Criteria
from useraccess.models import SchedulerUser
from residentrequests.models import ResidentRequests
from settings.models import Settings

def getWeekDelta(startDate, endDate):
    #assume that every rotation and the schedule itself starts on Wednesday, per Chris
    #the idea is that both of these variables should be DateTimeField objects and we should be able to get the difference in days
    difference = endDate.date() - startDate.date()
    delta = difference.days

    weeks = math.ceil(delta / 7) #we use ceiling to round up all days ex: if delta = 10 that should be considered 2 weeks
    return weeks

class StatusView(viewsets.ModelViewSet):
    serializer_class = StatusSerializer
    # queryset = AlgorithmStatus.objects.all()
    def get_queryset(self):
        scheduleStart = Settings.StartSchedule
        for resident in SchedulerUser.objects.all():
            if resident.AccessLevel != 'not applicable':
                requests = ResidentRequests.objects.get(pk=resident.email)
                requestOne = requests.requestOne
                requestTwo = requests.requestTwo
                requestThree = requests.requestThree
                weekOfRequestOne = str(getWeekDelta(scheduleStart, requestOne))
                weekOfRequestTwo = str(getWeekDelta(scheduleStart, requestTwo))
                weekOfRequestThree = str(getWeekDelta(scheduleStart, requestThree))

                resident.save()
        return AlgorithmStatus.objects.all()
