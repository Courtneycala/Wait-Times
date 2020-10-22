def hs_waitTimes():
    import requests
    import json
    import MouseTools
    hs = MouseTools.Park(MouseTools.ids.HS_ID)
    print(hs.get_name())
    #print(hs.get_attraction_wait_times_detailed())

    #Rock 'n' Roller Coaster
    rockin = MouseTools.Attraction(80010182)
    rockinName = rockin.get_name()
    rockinWT = str(rockin.get_wait_time())
    rockinOutput = str(rockinName + ": " + rockinWT)
    print(rockinOutput)

    #Toy Story Mania
    tsMania = MouseTools.Attraction(209857)
    tsManiaName = tsMania.get_name()
    tsManiaWT = str(tsMania.get_wait_time())
    tsManiaOutput = str(tsManiaName + ": " + tsManiaWT)
    print(tsManiaOutput)

    #Slinky Dog Dash
    slinky = MouseTools.Attraction(18904138)
    slinkyName = slinky.get_name()
    slinkyWT = str(slinky.get_wait_time())
    slinkyOutput = str(slinkyName + ": " + slinkyWT)
    print(slinkyOutput)
 
    #Tower of Terror
    terror = MouseTools.Attraction(80010218)
    terrorName = terror.get_name()
    terrorWT = str(terror.get_wait_time())
    terrorOutput = str(terrorName + ": " + terrorWT)
    print(terrorOutput)

    #Millineum Falcon
    falcon = MouseTools.Attraction(19263735)
    falconName = falcon.get_name()
    falconWT = str(falcon.get_wait_time())
    falconOutput = str(falconName + ": " + falconWT)
    print(falconOutput)

    #Rise of the Resistance
    rise = MouseTools.Attraction(19263736) 
    riseName = rise.get_name()
    riseWT = str(rise.get_wait_time())
    if riseWT == "None":
        riseWT = "0"
    riseOutput = str(riseName + ": " + riseWT)
    print(riseOutput)



hs_waitTimes()