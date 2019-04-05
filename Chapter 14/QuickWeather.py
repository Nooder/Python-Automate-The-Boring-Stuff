#! python3
# Chapter 14 - Get the weather forecast for the location provided
# USAGE: QuickWeather.py <location>     # Location to lookup

import json, requests, sys

# Compute location from command line arguments
if len(sys.argv) < 2:
    print("USAGE: QuickWeather.py <location>")
    sys.exit()

location = " ".join(sys.argv[1:])

# Download the JSON info from OpenWeatherMap
url = "api.openweathermap.org/data/2.5/weather?q=%s" % location

response = requests.get(url)
response.raise_for_status()

# Load JSON data in to a python variable
weatherData = json.loads(response.text)
# Print weather descriptions
w = weatherData['list']
# TODO: Needs api key to access this API