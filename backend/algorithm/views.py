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

global weekTable = []

def getWeekDelta(startDate, endDate):
    #assume that every rotation and the schedule itself starts on Wednesday, per Chris
    #the idea is that both of these variables should be DateTimeField objects and we should be able to get the difference in days
    difference = endDate - startDate
    delta = difference.days

    weeks = math.ceil(delta / 7) #we use ceiling to round up all days ex: if delta = 10 that should be considered 2 weeks
    return weeks

class StatusView(viewsets.ModelViewSet):
    serializer_class = StatusSerializer

    def get_queryset(self):
        scheduleStart = Settings.objects.get(pk=1).StartSchedule
        scheduleEnd = Settings.objects.get(pk=1).EndSchedule
        messageOne = AlgorithmStatus(Status='Adding resident requests to schedule')
        messageOne.save()
        counter = 0
        for resident in SchedulerUser.objects.all():
            if resident.AccessLevel != 'NA':
                weekTableRow = []
                weekTableRow.append(resident.email)
                pgy = ord(str(resident.AccessLevel)[3])
                weekTableRow.append(pgy)
                for i in range(52):
                    weekTableRow.append('')
                requests = ResidentRequests.objects.get(pk=resident.email)
                requestOne = requests.requestOne
                requestTwo = requests.requestTwo
                requestThree = requests.requestThree
                weekOfRequestOne = getWeekDelta(scheduleStart, requestOne)
                keyOne = str(weekOfRequestOne)
                weekOfRequestTwo = getWeekDelta(scheduleStart, requestTwo)
                keyTwo = str(weekOfRequestTwo)
                weekOfRequestThree = getWeekDelta(scheduleStart, requestThree)
                keyThree = str(weekOfRequestThree)
                resident.ResidentSchedule.update({keyOne: "VACATION"})
                resident.save()
                resident.ResidentSchedule.update({keyTwo: "VACATION"})
                resident.save()
                resident.ResidentSchedule.update({keyThree: "VACATION"})
                resident.save()
                counter++

        messageTwo = AlgorithmStatus(Status='Resident black out dates now added')
        messageTwo.save()

        for currentWeek in range (52):

        # will ignore element 0
        pgyNeeded = [0] * 6
        pgyAvailable = [0] * 6

        # loop through all criteria/rotations, ignoring those not used in current week
        # increasing pgyNeeded based on minimum required residents
        for rotations in Criteria.objects.all()::
            startWeek = getWeekDelta(scheduleStart, rotations.StartRotation)
            endWeek = getWeekDelta(scheduleStart, rotations.EndRotation)

            if startWeek <= currentWeek <= endWeek:
                pgy = ord(str(rotations.ResidentYear)[3]) #Force cast as int
                residentsNeeded = rotations.MinResident 
                pgyNeeded[pgy] = pgyNeeded[pgy] + residentsNeeded

        # loop through all residents, ignoring those not availabvle
        # increasing pgyAvailable for each available residents
        # assumes weekTable only has residents and not chief residents
        for resident in SchedulerUser.objects.all(): #this basically is the equivalent of iterating through users

            userSchedule = weekTable[resident]
            userInfo = userSchedule[0]

            userEmail = userInfo[0] # probably don't need this
            userPgy = int(userInfo[1]) # Force to int

            #add +1 because the first element is the userInfo
            content = userSchedule[currentWeek + 1]   #todo // what exactly ?
            if content != "VACATION": 
                pgyAvailable[userPgy] += 1

        # loop through and compare pgyNeeded to pgyAvailable.
        for pgy in range(1, 6):
            if pgyNeeded[pgy] > pgyAvailable[pgy]:
                short = pgyNeeded[pgy] - pgyAvailable[pgy]
                badCriteria.append("For week " + currentWeek + ", we are short " + short + "residents of PGY" + pgy)

        if(len(badCriteria) > 0):
        #I was thinking print to console for testing purposes, then we can render request like in views.py in a separate app to frontend alerting users.
            print("Bad Criteria")
            return False
        else:
            return True

        return AlgorithmStatus.objects.all()
