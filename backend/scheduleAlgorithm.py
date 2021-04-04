#!/usr/bin/env python
import os
import sys

def main():


def checkResidentAvailability(criteria):
    #not sure how to import criteria
    for criterion in criteria:
        int numWeek = getWeek(criterion)

        int pgy = criterion.ResidentYear #not sure how to get this but should be accessible

        int eligibleResidents = 0

        int residentsNeeded = criterion.MinResident #not sure how to get this

        #not sure how to import residents
        for resident in residents:
            content = resident.weeks[numWeek]
            if content != "BLACKOUT" and resident.pgy == pgy: #not sure how to get resident.pgy
                eligibleResidents++

            if eligibleResidents >= residentsNeeded:
                break
        
        if eligibleResidents < residentsNeeded:
            #alert user here that we don't have enough residents
            break

def getWeek(criterion):
    #assume that every criterion and the schedule itself starts on monday
    startDate = criterion.StartRotation

    scheduleStart = schedule.StartDate #not sure how to get starting date of schedule model

    #the idea is that both of these variables should be DateTimeField objects and we should be able to get the difference in days
    #this syntax is a compelte guess from internet searches
    delta = datetime.datetime.strptime(scheduleStart, datetimeFormat) - datetime.datetime.strptime(startDate, datetimeFormat)
    delta = delta.days

    weeks = delta / 7
    return weeks

def algorithm():
    for i in range(criteria.length): #length is a bit of a guess here, acting like criteria is an array 
        criterion = criteria[i]

        