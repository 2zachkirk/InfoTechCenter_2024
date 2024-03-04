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

# Variable to call the weather() once VRS(vehicle Response System) is determined
weatherAlert = weather()

def vehicleResponseSystem():
    if weatherAlert == "Snowing":
        print("\n National Weather Service has updated our alarm by 30 minutes because of the forecast of",weatherAlert,
              "weather conditions.")
        print("VRS has been engaged only allowing you to drive 50mph.")
    elif weatherAlert == "Blizzard":
        print("\nNational Weather Service has updated our alarm by 45 minutes because of the forecast of",weatherAlert,
              "weather conditions.")
        print("VRS has been engaged only allowing you to drive 40mph.")
    elif weatherAlert == "Raining":
        print("\nNational Weather Service has updated our alarm by 10 minutes because of the forecast of",weatherAlert,
              "weather conditions.")
        print("VRS has been engaged only allowing you to drive 60mph.")
    elif weatherAlert =="Thunderstorm":
        print("\nNational Weather Service has updated our alarm by 35 minutes because of the forecast of", weatherAlert,
              "weather conditions.")
        print("VRS had been engaged only allowing you to drive 55mph.")
    elif weatherAlert == "Foggy":
        print("\nNational Weather Service had updated our alarm by 10 minutes because of the forecast of",weatherAlert,
              "weather conditions.")
        print("VRS has been engaged only allowing you to drive 60mph.")
    elif weatherAlert == "Windy":
        print("\nNational Weather Service had updated our alarm by 15 minutes because of the forecast of",weatherAlert,
              "weather conditions.")
        print("VRS has been engaged only allowing you to drive 70mph.")
    elif weatherAlert =="Icy":
        print("\nNational Weather Service had updated our alarm by 60 minutes because of the forecast of", weatherAlert,
              "weather conditions.")
        print("VRS has been engaged only allowing you to drive 30mph.")
    else:
        print("\nNational Weather Service forecasts", weatherAlert,"weather conditions.")
        print("VRS has been disengaged! Drive at your own risk.")

vehicleResponseSystem()