
import MouseTools

def wt_is_none(attraction):

    ride = MouseTools.Attraction(attraction.get_id())
    waitTime = str(ride.get_wait_time())
    status = str(ride.get_status())

    if waitTime == "None":
        if status == "Closed":
            waitTime = "Closed"
        elif status == "Operating":
            waitTime = "0"

    return waitTime

