from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import StatusSerializer
from .models import AlgorithmStatus

import math
#from datetime import date
import datetime
from criteria.models import Criteria
from useraccess.models import SchedulerUser
from residentrequests.models import ResidentRequests
from settings.models import Settings

def getWeekDelta(startDate, endDate):
    #assume that every rotation and the schedule itself starts on Wednesday, per Chris
    #the idea is that both of these variables should be DateTimeField objects and we should be able to get the difference in days
    difference = endDate - startDate
    delta = difference.days

    weeks = math.ceil(delta / 7) #we use ceiling to round up all days ex: if delta = 10 that should be considered 2 weeks
    return weeks

class StatusView(viewsets.ModelViewSet):
    serializer_class = StatusSerializer
    # queryset = AlgorithmStatus.objects.all()
    def get_queryset(self):
        scheduleStart = Settings.objects.get(pk=1).StartSchedule
        messageOne = AlgorithmStatus(Status='Adding resident requests to schedule')
        messageOne.save()
        for resident in SchedulerUser.objects.all():
            if resident.AccessLevel != 'NA':
                requests = ResidentRequests.objects.get(pk=resident.email)
                requestOne = requests.requestOne
                requestTwo = requests.requestTwo
                requestThree = requests.requestThree
                weekOfRequestOne = str(getWeekDelta(scheduleStart, requestOne))
                weekOfRequestTwo = str(getWeekDelta(scheduleStart, requestTwo))
                weekOfRequestThree = str(getWeekDelta(scheduleStart, requestThree))
                resident.ResidentSchedule.update({weekOfRequestOne: "VACATION"})
                resident.save()
                resident.ResidentSchedule.update({weekOfRequestTwo: "VACATION"})
                resident.save()
                resident.ResidentSchedule.update({weekOfRequestThree: "VACATION"})
                resident.save()
        messageTwo = AlgorithmStatus(Status='Black out dates now added')
        messageTwo.save()
        return AlgorithmStatus.objects.all()
