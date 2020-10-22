

def ep_waitTimes():
    import requests
    import json
    import MouseTools
    wdw_dest = MouseTools.Destination(80007798)
    epcot = MouseTools.Park(80007838)

    print(epcot.get_name())
    #print(epcot.get_attraction_wait_times_detailed())

    #test track
    testTrack  = MouseTools.Attraction(80010199)
    ttName = testTrack.get_name()
    ttWaitTime = str(testTrack.get_wait_time())

    print(ttName + ": " +  ttWaitTime)

    #soarin
    soarin = MouseTools.Attraction(20194)
    soarinName = soarin.get_name()
    soarinWT = str(soarin.get_wait_time())
    print(soarinName + ": " +  soarinWT)

    #frozen
    frozen = MouseTools.Attraction(18375495)
    frozenName = frozen.get_name()
    frozenWT = str(frozen.get_wait_time())
    print(frozenName + ": " +  frozenWT)

    #spaceshipEarth
    spaceshipEarth = MouseTools.Attraction(80010191)
    spaceshipEarthName = spaceshipEarth.get_name()
    spaceshipEarthWT = str(spaceshipEarth.get_wait_time())
    print(spaceshipEarthName + ": " + spaceshipEarthWT)
    #print(epcot.get_attraction_wait_times_detailed())

ep_waitTimes()