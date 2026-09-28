# Write a Python script using requests to call the OpenWeatherMap API 
# (https://api.openweathermap.org/data/2.5/weather) for the city 'Ahmedabad' using your own API key, 
# and print the current temperature.

import requests

API_KEY = "YOUR_OPENWEATHERMAP_API_KEY"  # Replace with your actual OpenWeatherMap API key
CITY = "Ahmedabad"
URL = "https://api.openweathermap.org/data/2.5/weather"

params = {
    "q": CITY,
    "appid": API_KEY,
    "units": "metric"
}

response = requests.get(URL, params=params)

if response.status_code == 200:
    data = response.json()
    temp = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    print(f"City               : {CITY}")
    print(f"Current Temperature: {temp}°C")
    print(f"Feels Like         : {feels_like}°C")
else:
    print(f"Failed to fetch weather for {CITY}. Status code: {response.status_code}")
    print(f"API Message: {response.json().get('message', response.text)}")
