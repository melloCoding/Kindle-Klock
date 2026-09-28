import json
import requests

def getWeather():

    # get weather data from userConfig.json
    try:
        with open("../userConfig.json", 'r') as file:
            userConfig = json.load(file)
            print("Successfully loaded data:", file)
    except FileNotFoundError:
        print("Failed to load userConfig.json")
    except json.JSONDecodeError:
        print("Error: The file contains invalid JSON formatting.")

    # construct the open-meteo API URL using the information from the userConfig.json file
    apiURL = "https://api.open-meteo.com/v1/forecast?latitude=" + userConfig["weather"]["latitude"] + "&longitude=" + userConfig["weather"]["longitude"]+ "&daily=temperature_2m_max,temperature_2m_min,sunrise,sunset&current=temperature_2m,relative_humidity_2m&timezone=auto&forecast_days=1&wind_speed_unit="+ userConfig["weather"]["wind-speed-unit"] + "&temperature_unit=" + userConfig["weather"]["temperature-unit"]+ "&precipitation_unit=" + userConfig["weather"]["precipitation-unit"]

    response = requests.get(apiURL)
    if response.status_code == 200:
        weatherData = response.json()
        print("Successfully retrieved weather data")
        return(weatherData)
    else:
        print("Failed to retrieve weather data")
        return None
    