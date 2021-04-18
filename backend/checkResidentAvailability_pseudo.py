def checkResidentAvailability(criteria):
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
                pgys = int(criterion.ResidentYear) #Force cast as int should work but idk
                #Sure, i was testing this in interactive console and here is my conversion.
                switch = {
                    'PGY1': 0,
                    'PGY2': 1,
                    'PGY3': 2,
                    'PGY4': 3,
                    'PGY5': 4
                }
                pgy = switch.get(pgys, "invalid pgy")
                residentsNeeded = criterion.MinResident #test
                pgyNeeded[pgy] = pgyNeeded[pgy] + residentsNeeded

        # loop through all residents, ignoring those not availabvle
        # increasing pgyAvailable for each available residents
        # assumes weekTable only has residents and not chief residents
        for resident in range(len(weekTable)): #this basically is the equivalent of iterating through users

            userSchedule = weekTable[resident]
            userInfo = userSchedule[0]

            userEmail = userInfo[0] # probably don't need this
            userPgy = int(userInfo[1]) # Force to int

            #add +1 because the first element is the userInfo
            content = userSchedule[currentWeek + 1]   #todo // what exactly ?
            if content != "BLACKOUT": 
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
