from wtIsNone import wt_is_none 

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
    if ttWaitTime == "None":
        ttWaitTime = wt_is_none(testTrack)


    ttOutput = str(ttName + ": " +  ttWaitTime + "\n")

    #soarin
    soarin = MouseTools.Attraction(20194)
    soarinName = soarin.get_name()
    soarinWT = str(soarin.get_wait_time())
    if soarinWT == "None":
        soarinWT = wt_is_none(soarinWT)
    soarinOutput = str(soarinName + ": " +  soarinWT + "\n")

    #frozen
    frozen = MouseTools.Attraction(18375495)
    frozenName = frozen.get_name()
    frozenWT = str(frozen.get_wait_time())
    if frozenWT == "None":
        frozenWT = wt_is_none(frozen)
    frozenOutput = str(frozenName + ": " +  frozenWT + "\n")

    #spaceshipEarth
    spaceshipEarth = MouseTools.Attraction(80010191)
    spaceshipEarthName = spaceshipEarth.get_name()
    spaceshipEarthWT = str(spaceshipEarth.get_wait_time())
    spaceshipEarthOutput = str(spaceshipEarthName + ": " + spaceshipEarthWT + "\n")
    #print(epcot.get_attraction_wait_times_detailed())

    epcotOutput = ttOutput + soarinOutput + frozenOutput + spaceshipEarthOutput
    return epcotOutput

#print(ep_waitTimes())