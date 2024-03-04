print("\n******************************************************\n")

print("Weather Branch\n")

#Import Libraries Here
import random
from time import sleep

#Create a function that randomly chooses a weather from a list
def weather():
    weatherForecast = ("Snowing","Blizzard", "Raining","Thunderstorm", "Foggy", "Windy", "Icy","Sunny")
    weatherConditions = random.choice(weatherForecast)
    return weatherConditions


print(weather())