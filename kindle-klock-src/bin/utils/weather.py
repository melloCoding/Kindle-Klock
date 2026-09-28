import json
import requests
import time

def getWeather():

    # get weather data from userConfig.json
    try:
        with open("userConfig.json", 'r') as file:
            userConfig = json.load(file)
            print("Successfully loaded data:", file)
    except FileNotFoundError:
        print("Failed to load userConfig.json")
    except json.JSONDecodeError:
        print("Error: The file contains invalid JSON formatting.")

    # extract the userConfig data we need
    latitude = userConfig["weather"]["latitude"] 
    longitude = userConfig["weather"]["longitude"]
    windSpeedUnit = userConfig["weather"]["wind-speed-unit"]
    temperatureUnit = userConfig["weather"]["temperature-unit"]
    precipitationUnit = userConfig["weather"]["precipitation-unit"]

    # construct the open-meteo API URL using the information from the userConfig.json file
    apiURL = "https://api.open-meteo.com/v1/forecast?latitude=" + latitude + "&longitude=" + longitude + "&daily=temperature_2m_max,temperature_2m_min,sunrise,sunset,uv_index_max&current=temperature_2m,relative_humidity_2m&timezone=auto&forecast_days=1&wind_speed_unit="+ windSpeedUnit + "&temperature_unit=" + temperatureUnit + "&precipitation_unit=" + precipitationUnit

    # make the request using the constucted api url
    # no key is required because we are not an enterprise so open-meteo is free to us
    response = requests.get(apiURL)

    # Check if valid response recieved if so set weatherData to the response
    # Returns None if fail
    if response.status_code == 200:
        weatherData = response.json()
        print("Successfully retrieved weather data")
        return(weatherData)
    else:
        print("Failed to retrieve weather data")
        return None

def getFormattedWeather(weatherJSON):
    # strip the date information off of the time
    sunriseIsolatedTime = weatherJSON["daily"]["sunrise"][0][11:]
    sunsetIsolatedTime = weatherJSON["daily"]["sunset"][0][11:]

    # convert the time to a time_data struct
    sunriseTimeParsed = time.strptime(sunriseIsolatedTime, "%H:%M")
    sunsetTimeParsed = time.strptime(sunsetIsolatedTime, "%H:%M")

    # convert to 24 hour time
    sunriseFormatted = time.strftime("%I:%M %p", sunriseTimeParsed)
    sunsetFormatted = time.strftime("%I:%M %p", sunsetTimeParsed)

    cleanedWeatherJSON = {
        "temperature": weatherJSON["current"]["temperature_2m"],
        "humidity": weatherJSON["current"]["relative_humidity_2m"],

        "high": weatherJSON["daily"]["temperature_2m_max"][0],
        "low": weatherJSON["daily"]["temperature_2m_min"][0],
        "sunrise": sunriseFormatted,
        "sunset": sunsetFormatted,
        "uv-index-max": weatherJSON["daily"]["uv_index_max"][0]
    }

    # return the cleaned up json
    return cleanedWeatherJSON