print("**************************************************************")
print("Gasoline Branch\n\n")

# Import Libraries Here
import random

def gasLevelGauge():
    gasLevelList = ["Empty","Low","Quarter Tank","Half Tank","Three Quarter","Full Tank"]
    currentGasLevel = random.choice (gasLevelList)
    return currentGasLevel


print(gasLevelGauge())