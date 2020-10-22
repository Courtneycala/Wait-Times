
def mk_waitTimes(): 

   #import requests
   import json
   import MouseTools
   mk = MouseTools.Park(80007944)
   #print(mk.get_attraction_wait_times_detailed())
   print(mk.get_name())
   #pirates
   pirates = MouseTools.Attraction(80010177)
   piratesName = pirates.get_name()
   piratesWT = str(pirates.get_wait_time())
   piratesOutput = str(piratesName + ": " + piratesWT)
   print(piratesOutput)

   #space mtn
   spaceMtn = MouseTools.Attraction(80010190)
   spaceMtnName = spaceMtn.get_name()
   spaceMtnWT = str(spaceMtn.get_wait_time())
   spaceMtnOutput = str(spaceMtnName + ": " + spaceMtnWT)
   print(spaceMtnOutput)

   #big thunder
   thunderMtn = MouseTools.Attraction(80010110)
   thunderMtnName = thunderMtn.get_name()
   thunderMtnWT = str(thunderMtn.get_wait_time())
   thunderMtnOutput = str(thunderMtnName + ": " + thunderMtnWT)
   print(thunderMtnOutput)

   #splash mountain
   splashMtn = MouseTools.Attraction(80010192)
   splashMtnName = splashMtn.get_name()
   splashMtnWT = str(splashMtn.get_wait_time())
   if splashMtnWT == None:
      splashStatus = str(splashMtn.get_status())
      if splashStatus == "Closed":
         print("Splash is closed")
   splashMtnOutput = str(splashMtnName + ": " + splashMtnWT)
   print(splashMtnOutput)

mk_waitTimes()