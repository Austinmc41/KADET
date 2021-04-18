def checkResidentAvailability(criteria, users):
# what is the point of users as a parameter?

    global weekTable

    badCriteria = []

    # loop through entire year, week by week
    for currentWeek in range (52):

        # will ignore element 0
        pgyNeeded = [0] * 6
        pgyAvailable = [0] * 6

        # loop through all criteria/rotations, ignoring those not used in current week
        # increasing pgyNeeded based on minimum required residents
        for criterion in criteria:
            startWeek = getWeek(criterion.StartRotation)
            endWeek = getWeek(criterion.EndRotation)

            if startWeek <= currentWeek <= endWeek:
                pgy = criterion.ResidentYear #test; may need to be changed to make sure this is an integer and not a string
                residentsNeeded = criterion.MinResident #test
                pgyNeeded[pgy] = pgyNeeded[pgy] + residentsNeeded

        # loop through all residents, ignoring those not availabvle
        # increasing pgyAvailable for each available residents
        # assumes weekTable only has residents and not chief residents
        for resident in range(len(weekTable)): #this basically is the equivalent of iterating through users

            userSchedule = weekTable[resident]
            userInfo = userSchedule[0]

            userEmail = userInfo[0] # probably don't need this
            userPgy = userInfo[1] # may need to be changed to make sure this is an integer and not a string

            #add +1 because the first element is the user's email
            content = userSchedule[currentWeek + 1]   #todo
            if content != "BLACKOUT": 
                pgyAvailable[userPgy] += 1

        # loop through and compare pgyNeeded to pgyAvailable
        for pgy in range(1, 6):
            if pgyNeeded[pgy] > pgyAvailable[pgy]:
                short = pgyNeeded[pgy] - pgyAvailable[pgy]
                badCriteria.append("For week " + currentWeek + ", we are short " + short + "residents of PGY" + pgy)

    if(len(badCriteria) > 0):
    #ALERT USER WITH BADCRITERIA
        return False
    else:
        return True
