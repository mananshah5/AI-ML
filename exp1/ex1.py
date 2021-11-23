import random
import time


#This is a program that optimises battery health by balancing the battery requirements according to 
#urgency and the voltages for a long lasting battery 


def fetchBattery():

    #We can fetch the battery percentage from the phone
    #For now, a random battery percentage from 0 to 100 is assigned

    curr_battery = random.randint(0,100)
    print("\nCurrent battery: ",curr_battery,'%')
    if curr_battery<20:

        #SOS. Need fast charging.
        #We compromise battery health in exchange for fast charging

        print("Fast charging activated at 15V\n\n-----------------")
        
    if curr_battery>=20 and curr_battery<80:

        #Regular charging is sufficient.
        #This is a good balance of charging rate and battery health consideration

        print("Regular charging activated at 10V\n\n-----------------")

    if curr_battery>=80:

        #Relaxed charging is sufficient
        #We are in no urgency for battery. So we charge at a 
        #relaxed rate, in favour of battery health

        print("Relaxed charging activated at 5V\n\n-----------------")
    
while(True):
    fetchBattery()
    time.sleep(5)