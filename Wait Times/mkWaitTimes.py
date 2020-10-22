from wtIsNone import wt_is_none 

def mk_waitTimes(): 

   import requests
   import json
   import MouseTools
   mk = MouseTools.Park(80007944)
   #print(mk.get_attraction_wait_times_detailed())
   print(mk.get_name())
   #hours = mk.get_hours()

   #pirates
   pirates = MouseTools.Attraction(80010177)
   piratesName = pirates.get_name()
   piratesWT = str(pirates.get_wait_time())
   if piratesWT == "None":
      piratesWT = wt_is_none(pirates)

   piratesOutput = str(piratesName + ": " + piratesWT + "\n")
   #print(piratesOutput)

   #space mtn
   spaceMtn = MouseTools.Attraction(80010190)
   spaceMtnName = spaceMtn.get_name()
   spaceMtnWT = str(spaceMtn.get_wait_time())
   if spaceMtnWT == "None":
      spaceMtnWT = wt_is_none(spaceMtn)

   spaceMtnOutput = str(spaceMtnName + ": " + spaceMtnWT + "\n")
   #print(spaceMtnOutput)

   #big thunder
   thunderMtn = MouseTools.Attraction(80010110)
   thunderMtnName = thunderMtn.get_name()
   thunderMtnWT = str(thunderMtn.get_wait_time())
   if thunderMtnWT == "None":
      thunderMtnWT = wt_is_none(thunderMtn)

   thunderMtnOutput = str(thunderMtnName + ": " + thunderMtnWT + "\n")
   #print(thunderMtnOutput)

   #splash mountain
   splashMtn = MouseTools.Attraction(80010192)
   splashMtnName = splashMtn.get_name()
   splashMtnWT = str(splashMtn.get_wait_time())
   if splashMtnWT == "None":
      #splashStatus = str(splashMtn.get_status())
      #if splashStatus == "Closed":
         #splashMtnWT = "Closed"
      #elif splashStatus == "Operating":
         #splashMtnWT = "0"
      splashMtnWT = wt_is_none(splashMtn)
   splashMtnOutput = str(splashMtnName + ": " + splashMtnWT + "\n")
   #print(splashMtnOutput)

   magicOutput = piratesOutput + spaceMtnOutput + thunderMtnOutput + splashMtnOutput

   return magicOutput
   #return hours

#print(mk_waitTimes())