print("**************************************************************")
print("Gasoline Branch\n\n")

# Import Libraries Here
import random
from time import sleep 

#Function that lists gas levels, randomly choosing one and returning its value
def gasLevelGauge():
    gasLevelList = ["Empty","Low","Quarter Tank","Half Tank","Three Quarter","Full Tank"]
    currentGasLevel = random.choice (gasLevelList)
    return currentGasLevel

#Function that lists Gas stations, randomly choosing one and returning its value
def listOfGasStations():
    gasStations = ["Shell","Speedway","7Eleven","Marathon","Circle-K","Costco","Meijer","Valvoline"]
    gasStationsNearby = random.choice (gasStations)
    return gasStationsNearby

#Function will call the gasLevelGauge to determine our gas level and then find a close gas station
#by calling the listOfGasStations function if we are on Low or Quarter Tank
def gasLevelAlert():
    milesToGasStationsLow = round(random.uniform(1,25),1)
    milesToGasStationsQuarterTank = round(random.uniform(25.1,50),1)
    gasLevelIndicator = gasLevelGauge()
    if gasLevelIndicator == "Empty":
        print("***WARNING - YOU ARE ON EMPTY***")
        sleep(2.5)
        print("     ***Calling Triple AAA***")
    elif gasLevelIndicator == "Low":
        print("Your gas tank is extremely Low, checking Google Maps for the closest gas station...")
        sleep(2.5)
        print("The closest gas station is",listOfGasStations(),"Which is",milesToGasStationsLow,"miles away.")
    elif gasLevelIndicator == "Quarter Tank":
        print("Your gas tank is on a Quarter Tank, checking Google Maps for the closest gas station...")
        sleep(2.5)
        print("The closest gas station is",listOfGasStations(),"Which is",milesToGasStationsQuarterTank,"miles away.")
    elif gasLevelIndicator == "Half Tank":
        print("Your gas tank is a Half Tank full which is plenty to get to your destination.")
    elif gasLevelIndicator == "Three Quarter":
        print("Your gas tank is Three Quarter.")
    else:
        print("Your gas tank is at Full, No need to blow money today! Have fun and Drive free!")
        



gasLevelAlert()
