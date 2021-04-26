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
    difference = datetime.datetime(endDate) - datetime.datetime(startDate)
    delta = difference.days

    weeks = math.ceil(delta / 7) #we use ceiling to round up all days ex: if delta = 10 that should be considered 2 weeks
    return weeks

class StatusView(viewsets.ModelViewSet):
    serializer_class = StatusSerializer
    # queryset = AlgorithmStatus.objects.all()
    def get_queryset(self):
        scheduleStart = Settings.StartSchedule
        messageOne = AlgorithmStatus(Status='Adding resident requests to schedule')
        messageOne.save()
        for resident in SchedulerUser.objects.all():
            if resident.AccessLevel != 'NA':
                loopMessage = AlgorithmStatus(Status='looking up user ' + str(resident.email) + ' with access level ' + str(resident.AccessLevel))
                loopMessage.save()
                requests = ResidentRequests.objects.get(pk=resident.email)
                requestOne = requests.requestOne
                requestTwo = requests.requestTwo
                requestThree = requests.requestThree

                loopMessage2 = AlgorithmStatus(Status='{ ' + str(requestOne) + ' }, ' + 'type: ' + str(type(requestOne)))
                loopMessage2.save()
                loopMessage3 = AlgorithmStatus(Status='{ ' + str(scheduleStart) + ' }, ' + 'type: ' + str(type(scheduleStart)))
                loopMessage3.save()
                loopMessage4 = AlgorithmStatus(Status='{ ' + str(requests.email) + ' }, ' + 'type: ' + str(type(requests.email)))
                loopMessage4.save()

                weekOfRequestOne = str(getWeekDelta(scheduleStart, requestOne))
                weekOfRequestTwo = str(getWeekDelta(scheduleStart, requestTwo))
                weekOfRequestThree = str(getWeekDelta(scheduleStart, requestThree))
                resident.ResidentSchedule.update({weekOfRequestOne: "VACATION"})
                resident.save()
        messageTwo = AlgorithmStatus(Status='Black out dates now added')
        messageTwo.save()
        return AlgorithmStatus.objects.all()
