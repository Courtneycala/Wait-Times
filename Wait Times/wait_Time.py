

from mkWaitTimes import mk_waitTimes
from epcotWaitTimes import ep_waitTimes
from hsWaitTimes import hs_waitTimes
from akWaitTimes import ak_waitTimes
from wtIsNone import wt_is_none 

def wait_Time(park):
    import requests
    import json
    import MouseTools
    #print(park)
    
    
    
    
    if park == 1:
        magic = mk_waitTimes()
        print(magic)

    elif park == 2:
        epcot = ep_waitTimes()
        print(epcot)

    elif park == 3:
        hollywood = hs_waitTimes()
        print(hollywood)

    elif park == 4:
        
        animal = ak_waitTimes()
        print(animal)

    


wait_Time(1)
