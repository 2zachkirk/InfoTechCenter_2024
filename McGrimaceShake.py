print("**************************************************************")
print("Gasoline Branch\n\n")

# Import Libraries Here
import random

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


print(gasLevelGauge())
print(listOfGasStations())