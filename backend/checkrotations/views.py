from django.shortcuts import render

from rest_framework import viewsets
from .serializers import RotationStatusSerializer
from .models import RotationStatus

class RotationStatusView(viewsets.ModelViewSet):
    serializer_class = RotationStatusSerializer

    def get_queryset(self):

        weeks = 52
        rotations = []
        rotationMinMax = {}
        essentialRotations = []
        overnightRotations = []
        otherRotations = []
        rotationWeeks = {}
        pgyRotation = {}

        weekTable = []

        RotationStatus.objects.all().delete()
        scheduleStart = Settings.objects.get(pk=1).StartSchedule
        messageOne = RotationStatus(Status='Adding resident requests to schedule')
        messageOne.save()

        for resident in SchedulerUser.objects.all():
            if resident.AccessLevel != 'NA':
                weekTableRow = []
                weekTableRow.append(resident.email)
                pgy = int(resident.AccessLevel)
                weekTableRow.append(pgy)
                for i in range(52):
                    weekTableRow.append('available')
                weekTable.append(weekTableRow)

        for requests in VacationRequests.objects.all():

            resident = SchedulerUser.objects.get(email=requests.email)

            for week in range (weeks): # clears resident's schedule
                resident.ResidentSchedule.update({week: "available"})
                requests.save()

            userSchedule = []
            residentFound = False
            counter = -1
            while not residentFound:
                counter += 1
                userSchedule = weekTable[counter]
                residentFound = (str(userSchedule[0]) == str(requests.email))
            requestOne = requests.requestOne
            requestTwo = requests.requestTwo
            requestThree = requests.requestThree
            weekOfRequestOne = getWeekDelta(scheduleStart, requestOne)
            weekOfRequestTwo = getWeekDelta(scheduleStart, requestTwo)
            weekOfRequestThree = getWeekDelta(scheduleStart, requestThree)
            resident.ResidentSchedule.update({weekOfRequestOne: "VACATION"})
            resident.save()
            resident.ResidentSchedule.update({weekOfRequestTwo: "VACATION"})
            resident.save()
            resident.ResidentSchedule.update({weekOfRequestThree: "VACATION"})
            resident.save()

            userSchedule[weekOfRequestOne + 2] = "VACATION"
            userSchedule[weekOfRequestTwo + 2] = "VACATION"
            userSchedule[weekOfRequestThree + 2] = "VACATION"

        messageTwo = RotationStatus(Status='Resident black out dates now added')
        messageTwo.save()

        errorCounter = 0
        for currentWeek in range (weeks):

            # will ignore element 0
            pgyNeeded = [0] * 6
            pgyAvailable = [0] * 6

            # loop through all criteria/rotations, ignoring those not used in current week
            # increasing pgyNeeded based on minimum required residents
            for rotation in Criteria.objects.all():
                startWeek = getWeekDelta(scheduleStart, rotation.StartRotation)
                endWeek = getWeekDelta(scheduleStart, rotation.EndRotation)
                pgy = int(resident.AccessLevel)
                if startWeek <= currentWeek <= endWeek:
                    residentsNeeded = rotation.MinResident 
                    pgyNeeded[pgy] = pgyNeeded[pgy] + residentsNeeded

            # loop through all residents, ignoring those not availabvle
            # increasing pgyAvailable for each available residents
            # assumes weekTable only has residents and not chief residents
            for resident in range(len(weekTable)): #this basically is the equivalent of iterating through users
                userSchedule = weekTable[resident]
                userPgy = userSchedule[1]

                #add +2 because beginning elements are the user info
                rotation = userSchedule[currentWeek + 2]
                if rotation == 'available':
                    pgyAvailable[userPgy] += 1

            # loop through and compare pgyNeeded to pgyAvailable.
            for pgy in range(1, 6):
                if pgyNeeded[pgy] > pgyAvailable[pgy]:
                    errorCounter += 1
                    short = pgyNeeded[pgy] - pgyAvailable[pgy]
                    message = RotationStatus(Status="For week " + str(currentWeek) + ", we are short " + str(short) + " residents of PGY" + str(pgy))
                    message.save()
        if errorCounter == 0:
            message = RotationStatus(Status="Resident availability check successful")
            message.save()
