from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import StatusSerializer
from .models import AlgorithmStatus

import math
import pulp
import datetime
from criteria.models import Criteria
from useraccess.models import SchedulerUser
from residentrequests.models import ResidentRequests
from settings.models import Settings

#to hold finished schedule
global weekTable

#information/constraints needed for scheduling algorithm
global weeks
global residents
global rotations
global rotationMinMax
global rotationType
global rotationWeeks
global pgyRotation
global pgyResident
global unavailable

weeks = 9
residents = []
rotations = []
rotationMinMax = {}
rotationType = {}
rotationWeeks = {}
pgyRotation = {}
pgyResident = {}
unavailable = {}
weekTable = []

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
        AlgorithmStatus.objects.all().delete()
        scheduleStart = Settings.objects.get(pk=1).StartSchedule
        #scheduleEnd = Settings.objects.get(pk=1).EndSchedule
        messageOne = AlgorithmStatus(Status='Adding resident requests to schedule')
        messageOne.save()
        for resident in SchedulerUser.objects.all():
            if resident.AccessLevel != 'NA':
                residents.append(resident.email) #for algorithm
                weekTableRow = []
                weekTableRow.append(resident.email)
                pgy = int(str(resident.AccessLevel)[3])
                pgyResident.update({resident.email: pgy}) #for algorithm
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
                weekTableRow[weekOfRequestOne + 2] = "VACATION"
                weekTableRow[weekOfRequestTwo + 2] = "VACATION"
                weekTableRow[weekOfRequestThree + 2] = "VACATION"
                weekTable.append(weekTableRow)
                unavailable.update({resident.email: [weekOfRequestOne, weekOfRequestTwo, weekOfRequestThree]}) #for algorithm

        messageTwo = AlgorithmStatus(Status='Resident black out dates now added')
        messageTwo.save()

        errorCounter = 0
        #rotationCounter = 0
        for currentWeek in range (52):

            # will ignore element 0
            pgyNeeded = [0] * 6
            pgyAvailable = [0] * 6

            # loop through all criteria/rotations, ignoring those not used in current week
            # increasing pgyNeeded based on minimum required residents
            for rotation in Criteria.objects.all():
                startWeek = getWeekDelta(scheduleStart, rotation.StartRotation)
                endWeek = getWeekDelta(scheduleStart, rotation.EndRotation)
                pgy = int(str(rotation.ResidentYear)[3]) #Force cast as int
                if startWeek <= currentWeek <= endWeek:
                    
                    residentsNeeded = rotation.MinResident 
                    pgyNeeded[pgy] = pgyNeeded[pgy] + residentsNeeded
                #for algorithm
                #if rotationCounter == 0:
                rotations.append(rotation.RotationType)
                rotationMinMax.update({rotation.RotationType: (rotation.MinResident, rotation.MaxResident)})
                rotationType.update({rotation.RotationType: (rotation.Essential, rotation.Overnight)})
                rotationWeeks.update({rotation.RotationType: [i for i in range(startWeek, endWeek + 1)]})
                pgyRotation.update({rotation.RotationType: pgy})
                #print("rot pgy: " + str(pgy) + " " + rotation.RotationType)
            #rotationCounter += 1

            # loop through all residents, ignoring those not availabvle
            # increasing pgyAvailable for each available residents
            # assumes weekTable only has residents and not chief residents
            for resident in range(len(weekTable)): #this basically is the equivalent of iterating through users

                userSchedule = weekTable[resident]
                #userEmail = userSchedule[0]
                userPgy = userSchedule[1]

                #add +2 because beginning elements are the user info
                rotation = userSchedule[currentWeek + 2]
                if rotation == '':
                    pgyAvailable[userPgy] += 1

            # loop through and compare pgyNeeded to pgyAvailable.
            for pgy in range(1, 6):
                if pgyNeeded[pgy] > pgyAvailable[pgy]:
                    errorCounter += 1
                    short = pgyNeeded[pgy] - pgyAvailable[pgy]
                    message = AlgorithmStatus(Status="For week " + str(currentWeek) + ", we are short " + str(short) + " residents of PGY" + str(pgy))
                    message.save()
        if errorCounter == 0:
            message = AlgorithmStatus(Status="Resident availability check successful")
            message.save()

        # PuLP 'problem'
        problem = pulp.LpProblem("resident scheduler", pulp.LpMaximize)

        # PuLP variables
        assignments = pulp.LpVariable.dicts("Assignments", ((week, resident, rotation) for week in range(weeks) for resident in residents for rotation in rotations), cat="Binary")
        is_assigned = pulp.LpVariable.dicts("Is Assigned", residents, cat="Binary")

        # PuLP constraints
        for week in range(weeks):
            for rotation in rotations:
                #print(str(rotation) + str(rotationWeeks[rotation]))
                if week in rotationWeeks[rotation]:
                    # In every week, each rotation is assigned by min/max required residents
                    problem += pulp.lpSum(assignments[week, resident, rotation] for resident in residents) >= rotationMinMax[rotation][0] #min
                    #print(str(rotation) + str(rotationMinMax[rotation][0]))
                    #problem += pulp.lpSum(assignments[week, resident, rotation] for resident in residents) <= rotationMinMax[rotation][1] #max
                #else:
                    #problem += pulp.lpSum(assignments[week, resident, rotation] for resident in residents) == 0

            for resident in residents:
                # Nobody is assigned multiple rotations in the same week
                problem += pulp.lpSum(assignments[week, resident, rotation] for rotation in rotations) <= 1
                # residents with incorrect PGY level are not available for rotation
                for rotation in rotations:
                    #print(str(pgyRotation[rotation]) + " : " + str(pgyResident[resident]))
                    if week in rotationWeeks[rotation] and (pgyRotation[rotation] != pgyResident[resident]):
                        problem += assignments[week, resident, rotation] == 0

        for resident, blockedOut in unavailable.items():
            for week in blockedOut:
                if week <= weeks:
                    for rotation in rotations:
                        # Nobody is assigned a rotation in a week they are unavailable
                        problem += assignments[week, resident, rotation] == 0

        # Constrain 'is_assigned' auxiliary variable
        for week in range(weeks):
            for resident in residents:
                for rotation in rotations:
                    problem += is_assigned[resident] >= assignments[week, resident, rotation]

        for resident in residents:
            problem += is_assigned[resident] <= pulp.lpSum(assignments[week, resident, rotation] for week in range(weeks) for rotation in rotations)

        # PuLP objective
        problem += pulp.lpSum(is_assigned[resident] for resident in residents)

        # Solve with the Coin/Cbc solver
        #tempMessage = AlgorithmStatus(Status=str(pulp.listSolvers(onlyAvailable=True)))
        #tempMessage.save()
        problem.solve(pulp.PULP_CBC_CMD(msg=1))

        for week in range(weeks):
            #print(f"week {week}:")
            for rotation in rotations:
                for resident in residents:
                    if pulp.value(assignments[week, resident, rotation]) == 1:
                        #print(f"    {rotation}: {resident}")
                        message = AlgorithmStatus(Status="For week " + str(week) + ", " + str(resident) + " is assigned to " + str(rotation))
                        message.save()

        return AlgorithmStatus.objects.all()
