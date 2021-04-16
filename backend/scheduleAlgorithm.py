#!/usr/bin/env python
import os
import sys
# importing Criteria importing model for Criteria
from criteria.models import Criteria
from useraccess.models import SchedulerUser

eligibilityTable = []

weekTable = []
#week table will essentially be the 2D list of resident weeks
#list of lists, each individual list is a singular resident's schedule week by week

# main flow of the program is here
def main():
    all_Criteria = Criteria.objects.all()
    # converting queryset to list for easier traversal and indexing
    criteriaList = list(all_Criteria)
    # converting queryset to list for easier traversal and indexing
    all_Users = SchedulerUser.objects.all()
    userList = list(all_Users)

    #copy pasted Austin's queryset translation here, hope it works
    all_Requests = ResidentRequests.objects.all()
    requestList = list(all_Requests)

    generateWeekTable(requestList)

    checkResidentAvailability(criteriaList, userList)

    if(checkResidentAvailability == True):
        algorithm(criteriaList, userList)

def generateWeekTable(requestList):
    global weekTable

    #not sure how to get this, this could hypothetically just be 52 but this makes it more flexible
    scheduleLength = getWeekLength(schedule.startDate, schedule.endDate)

    #one issue here is that the 2D array will have its users sorted by request. thus we'll have the user email at the top of the list
    for request in requestList:
        #guessing the syntax here
        requestOne = request.requestOne
        requestTwo = request.requestTwo
        requestThree = request.requestThree

        #changed getWeek to take in a dateField instead of a criteria
        #at the moment assuming that every request will be honored, not 100% sure if that is how it is though
        requestWeekOne = getWeek(requestOne)
        requestWeekTwo = getWeek(requestTwo)
        requestWeekThree = getWeek(requestThree)

        #don't think requests even holds the PGY info atm, but it makes this easier
        userInfo = [request.email, request.pgy]
        #make the first element of the list the userInfo
        #it's possible that it's more efficient to use a dictionary, feel free to swap things up if you wanna go with that
        userSchedule = [userInfo]
        for i in range(scheduleLength):
            #assuming we start at week 0, as i believe that is how getWeek will work, check my logic
            if i == requestWeekOne:
                userSchedule.append("BLACKOUT")
            elif i == requestWeekTwo:
                userSchedule.append("BLACKOUT")
            elif i == requestWeekThree:
                userSchedule.append("BLACKOUT")
            else:
                userSchedule.append("NA")
        weekTable.append(userSchedule)


# takes in a list of criteria and users to check if availabilty of residents 
def checkResidentAvailability(criteria, users):
    #my python's a lil rusty, but from what ive googled, i need to declare eligibilityTable as a global for its values to change globally
    global eligibilityTable

    global weekTable

    badCriteria = []

    #not sure how to import criteria
    for i in range(len(criteria)): #length is a bit of a guess here, acting like criteria is an array 
        criterion = criteria[i]

        int startWeek = getWeek(criterion.StartRotation) 

        int numWeeks = getWeekLength(criterion.StartRotation, criterion.EndRotation)

        int pgy = criterion.ResidentYear #test

        int residentsNeeded = criterion.MinResident #test

        criterionEligibility = []

        #this basically is the equivalent of iterating through users
        for k in range(len(weekTable)):

            #use weeksAvailable to see if resident is available all weeks of criteria
            int weeksAvailable = 0

            userSchedule = weekTable[k]
            userInfo = weekTable[0]

            userEmail = userInfo[0]
            userPgy = userInfo[1]

            for j in range(numWeeks):
                
                #do startWeek to get week of criteria, add j to get exact week, add +1 because the first element is the user's email
                content = userSchedule[startWeek + j + 1]   #todo
                if content != "BLACKOUT" and userPgy == pgy: 
                    weeksAvailable++
            
            if weeksAvailable == numWeeks:
                #append userEmail now
                criterionEligibility.append(userInfo)

        if criterionEligibility.length < residentsNeeded:
            #append criterion to badCriteria if not enough
            badCriteria.append(criterion)

        eligibilityTable.append(criterionEligibility)

        if criterion.isEssential() and i > 0:
            #checks if i > 0 because we're about to do i - 1
            prevCriterion = criteria[i - 1]
            prevMin = prevCriterion.MinResident
            if(prevCriterion.isOvernight()):
                numUnique = getUniqueResidents(i, i - 1).length
                if(numUnique < (prevMin + residentsNeeded)):
                    #append criterion to badCriteria if not enough
                    badCriteria.append(criterion)

    if(len(badCriteria) > 0):
        #ALERT USER WITH BADCRITERIA
        return False
    else:
        return True

def getWeek(startDate):
    #assume that every criterion and the schedule itself starts on monday

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

# takes in a list of criteria and users 
def algorithm(criteria, users):
    global eligibilityTable

    global weekTable

    for i in range(len(criteria)): 
        #iterate through criteria
        criterion = criteria[i]

        int residentsNeeded = criterion.MinResident

        int startWeek = getWeek(criterion.StartRotation) 

        int numWeeks = getWeekLength(criterion.StartRotation, criterion.EndRotation)

        #changed things up because weekTable is organized by the users in the the request list
        #basically you iterate through weekTable and if you see a user that was eligible for the criteria, you add them to the criteria
        #ends early if you get the number of residentsNeeded
        int residentsAcquired = 0
        for userSchedule in weekTable:

            userInfo = userSchedule[0]
            if userInfo in eligibilityTable[i]:
                residentsAcquired++
                for j in range(numWeeks):
                    #+1 here cuz the first element is userInfo
                    userSchedule[startWeek + j + 1] = criterion.RotationType
            
            if residentsAcquired == residentsNeeded:
                break

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

                #TODO: update this section below where you unassign and assign residents with respect to the new weekTable system

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