

def ak_waitTimes():
    import requests
    import json
    import MouseTools
    wdw_dest = MouseTools.Destination(80007798)
    ak = MouseTools.Park(80007823)
    print(ak.get_name())
    #print(ak.get_attraction_wait_times_detailed())

    #Kilimanjaro Safari
    safari = MouseTools.Attraction(80010157)
    safariName = safari.get_name()
    safariWT = str(safari.get_wait_time())
    safariOutput = str(safariName + ": " + safariWT)
    print(safariOutput)

    #Everest
    everest = MouseTools.Attraction(26068)
    everestName = everest.get_name()
    everestWT = str(everest.get_wait_time())
    safariOutput = str(everestName + ": " + everestWT)
    print(safariOutput)

    #Kali River Rapids
    kali = MouseTools.Attraction(80010154)
    kaliName = kali.get_name()
    kaliWT = str(kali.get_wait_time())
    kaliOutput = str(kaliName + ": " + kaliWT)
    print(kaliOutput)

    #Avatar
    avatar = MouseTools.Attraction(18665186)
    avatarName = avatar.get_name()
    avatarWT = str(avatar.get_wait_time())
    avatarOutput = str(avatarName + ": " + avatarWT)
    print(avatarOutput)


ak_waitTimes()