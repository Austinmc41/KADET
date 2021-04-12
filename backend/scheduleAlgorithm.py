#!/usr/bin/env python
import os
import sys
# importing Criteria importing model for Criteria
from criteria.models import Criteria
from useraccess.models import SchedulerUser

eligibilityTable = []

def main():
    all_Criteria = Criteria.objects.all() 
    all_Users = SchedulerUser.objects.all()
    checkResidentAvailability(all_Criteria, all_Users)

def checkResidentAvailability(criteria, users):
    #my python's a lil rusty, but from what ive googled, i need to declare eligibilityTable as a global for its values to change globally
    global eligibilityTable

    #not sure how to import criteria
    for i in range(len(criteria): #length is a bit of a guess here, acting like criteria is an array 
        criterion = criteria[i]

        int startWeek = getWeek(criterion) 

        int pgy = criterion.ResidentYear #test

        int residentsNeeded = criterion.MinResident #test

        int numWeeks = getWeekLength(criterion.StartRotation, criterion.EndRotation)

        criterionEligibility = []

        #not sure how to import residents
        for user in users:

            #use weeksAvailable to see if resident is available all weeks of criteria
            int weeksAvailable = 0
            for j in range(numWeeks):
                if user.ACCESS_CHOICES != "not applicable"  
                    #do startWeek to get week of criteria, add j to get exact week
                    content = resident.weeks[startWeek + j]   #todo
                    if content != "BLACKOUT" and resident.pgy == pgy: #not sure how to get resident.pgy
                        weeksAvailable++
            
            if weeksAvailable == numWeeks:
                criterionEligibility.append(user)

        if criterionEligibility.length < residentsNeeded:
            #alert user here that we don't have enough residents
            break

        eligibilityTable.append(criterionEligibility)

        if criterion.isEssential() and i > 0:
            #checks if i > 0 because we're about to do i - 1
            prevCriterion = criteria[i - 1]
            prevMin = prevCriterion.MinResident
            if(prevCriterion.isOvernight()):
                numUnique = getUniqueResidents(i, i - 1).length
                if(numUnique < (prevMin + residentsNeeded)):
                    #ALERT USER
                    break

def getWeek(Criteria):
    #assume that every criterion and the schedule itself starts on monday
    startDate = criterion.StartRotation

    scheduleStart = schedule.StartDate #not sure how to get starting date of schedule model

    #the idea is that both of these variables should be DateTimeField objects and we should be able to get the difference in days
    #this syntax is a compelte guess from internet searches
    delta = datetime.datetime.strptime(scheduleStart, datetimeFormat) - datetime.datetime.strptime(startDate, datetimeFormat)
    delta = delta.days

    weeks = delta / 7
    return weeks

def getWeekLength(startDate, endDate):

    #the idea is that both of these variables should be DateTimeField objects and we should be able to get the difference in days
    #this syntax is a compelte guess from internet searches
    delta = datetime.datetime.strptime(endDate, datetimeFormat) - datetime.datetime.strptime(startDate, datetimeFormat)
    delta = delta.days

    weeks = delta / 7
    return weeks

def getUniqueResidents(i, i2):
    #arguments: indices of table to get unique residents from
    global eligibilityTable

    uniqueResidents = eligibilityTable[i]

    for resident in eligibilityTable[i2]:
        if resident not in uniqueResidents:
            uniqueResidents.append(resident)

    return uniqueResidents

def algorithm():
    global eligibilityTable

    for i in range(criteria.length): 
        #iterate through criteria
        criterion = criteria[i]

        int residentsNeeded = criterion.MinResident

        for j in range(residentsNeeded):
            #this basically assigns the first residentsNeeded residents into the criteria
            #assigns resident by changing week[i] value
            assignedResident = eligibilityTable[i][j]
            assignedResident.weeks[i] = criterion.RotationType

        if criterion.isEssential() and i > 0:
            #if the criterion is essential, we have to check if the previous one is overnight
            prevCriterion = criteria[i - 1]
            prevMin = prevCriterion.MinResident

            if(prevCriterion.isOvernight()):
                #the only way we run out of students is if the people assigned to the overnight were the only people 
                #available for the essential, with numerous other people available for the overnight

                #thus, we basically check if essential has enough people if we remove the people assigned to overnight previously
                #we're going to remove the overnight assigned people from the essential list
                #thus, we're going to make a copy of the eligible residents for the essential rotation and remove the overnight people
                
                #now, i would like to do this calculation with just basic math regarding number of residents required
                #it may be possible, i'm just worried about unique residents and whether some residents are eligible for both overnight and essential
                eligibleEssential = eligibilityTable[i].copy()
                eligibleOvernight = eligibilityTable[i - 1]
                for k in range(prevMin):
                    overnightResident = eligibleOvernight[k]
                    if overnightResident in eligibleEssential:
                        #if the overnightResident is even in the eligible list, then remove
                        eligibleEssential.remove(overnightResident)

                numEssential = eligibleEssential.length

                #now we check if the number of remaining people is enough
                if numEssential < residentsNeeded:
                    #if the num remaining people isn't enough, we then assign with priority to the essential rotation
                    #the first x residents are already assigned to the essential rotation given the above code
                    #thus, all we have to do are to remove the first x residents from the previous rotation and to assign the next x
                    for x in range(prevMin):
                        resident = eligibilityTable[i - 1][x]
                        resident.week[i - 1] = None
                    for x in range(prevMin):
                        resident = eligibilityTable[i - 1][x + prevMin]
                        resident.week[i - 1] = None
                    #CHECK LOGIC HERE, its possible that at least one of the prevMin should actually be residentsNeeded