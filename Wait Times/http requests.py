import requests
import json
import MouseTools

wdw_dest = MouseTools.Destination(80007798)
print(wdw_dest.get_park_ids())

# sync_on_init means sync the database with Disney on object instantiation. Default is True.
# This parameter is helpful when creating many objects back to back as syncing only once is necessary.
dlr_dest = MouseTools.Destination(80008297, sync_on_init=True)
#Sprint(dlr_dest.get_attraction_ids())

mk = MouseTools.Park(80007944)
print(mk.get_wait_times())

pirates = MouseTools.Attraction(80010177)
print(pirates.get_wait_time())


# You don't have to know any ids to get started.
MouseTools.ids.WDW_ID     # Walt Disney World Resort
MouseTools.ids.DLR_ID     # Disneyland Resort

# Single park ids
MouseTools.ids.MK_ID      # Magic Kingdom
MouseTools.ids.EPCOT_ID   # EPCOT
MouseTools.ids.HS_ID      # Hollywood Studios
MouseTools.ids.AK_ID      # Animal Kingdom
MouseTools.ids.TL_ID      # Typhoon Lagoon
MouseTools.ids.BB_ID      # Blizzard Beach
MouseTools.ids.DLP_ID     # Disneyland Park
MouseTools.ids.CA_ID      # California Adventure

# List of ids
# Parks
MouseTools.ids.WDW_PARK_IDS
MouseTools.ids.DLR_PARK_IDS

# Entertainment Venues
MouseTools.ids.WDW_EV_IDS
MouseTools.ids.DLR_EV_IDS

# Attractions
MouseTools.ids.WDW_ATTRACTION_IDS
MouseTools.ids.DLR_ATTRACTION_IDS

# Entertainments
MouseTools.ids.WDW_ENTERTAINMENT_IDS
MouseTools.ids.DLR_ENTERTAINMENT_IDS