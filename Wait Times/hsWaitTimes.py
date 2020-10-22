from wtIsNone import wt_is_none 

def hs_waitTimes():
    import requests
    import json
    import MouseTools
    hs = MouseTools.Park(MouseTools.ids.HS_ID)
    print(hs.get_name())
    #detailedWT = hs.get_attraction_wait_times_detailed()

    #Rock 'n' Roller Coaster
    rockin = MouseTools.Attraction(80010182)
    rockinName = rockin.get_name()
    rockinWT = str(rockin.get_wait_time())
    if rockinWT == "None":
        rockinWT = wt_is_none(rockin)
    rockinOutput = str(rockinName + ": " + rockinWT + "\n")
    #print(rockinOutput)

    #Toy Story Mania
    tsMania = MouseTools.Attraction(209857)
    tsManiaName = tsMania.get_name()
    tsManiaWT = str(tsMania.get_wait_time())
    if tsManiaWT == "None":
        tsManiaWT = wt_is_none(tsMania)
    tsManiaOutput = str(tsManiaName + ": " + tsManiaWT + "\n")
    #print(tsManiaOutput)

    #Slinky Dog Dash
    slinky = MouseTools.Attraction(18904138)
    slinkyName = slinky.get_name()
    slinkyWT = str(slinky.get_wait_time())
    if slinkyWT == "None":
        slinkyWT = wt_is_none(slinky)
    slinkyOutput = str(slinkyName + ": " + slinkyWT + "\n")
    #print(slinkyOutput)
 
    #Tower of Terror
    terror = MouseTools.Attraction(80010218)
    terrorName = terror.get_name()
    terrorWT = str(terror.get_wait_time())
    if terrorWT == "None":
        terrorWT = wt_is_none(terror)

    terrorOutput = str(terrorName + ": " + terrorWT + "\n")
    #print(terrorOutput)

    #Millineum Falcon
    falcon = MouseTools.Attraction(19263735)
    falconName = falcon.get_name()
    falconWT = str(falcon.get_wait_time())
    if falconWT == "None":
        falconWT = wt_is_none(falcon)
    falconOutput = str(falconName + ": " + falconWT + "\n")
    #print(falconOutput)


    #Mickey & Minnie
    mickey = MouseTools.Attraction(19259335)
    mickeyName = mickey.get_name()
    mickeyWT = str(mickey.get_wait_time())
    if mickeyWT == "None":
        mickeyWT = wt_is_none(mickey)
    mickeyOutput = str(mickeyName + ": " + mickeyWT + "\n")

    #Rise of the Resistance
    rise = MouseTools.Attraction(19263736) 
    riseName = rise.get_name()
    riseWT = str(rise.get_wait_time())
    if riseWT == "None":
        riseWT = wt_is_none(rise)
    riseOutput = str(riseName + ": " + riseWT + "\n")
    #print(riseOutput)

    hollywoodOutput = rockinOutput +  tsManiaOutput + slinkyOutput + terrorOutput + falconOutput + mickeyOutput + riseOutput
    return hollywoodOutput
    #return detailedWT



#print(hs_waitTimes())