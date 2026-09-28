# Fetch the current temperature and weather description for your city using the OpenWeatherMap 
# API and print the results in a readable format.

import requests

def get_weather(city="Ahmedabad", api_key="YOUR_OPENWEATHERMAP_API_KEY"):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    
    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            temp = data["main"]["temp"]
            weather_desc = data["weather"][0]["description"].title()
            humidity = data["main"]["humidity"]
            print(f"=== Weather Report for {city} ===")
            print(f"Temperature : {temp}°C")
            print(f"Description : {weather_desc}")
            print(f"Humidity    : {humidity}%")
        else:
            # Fallback demonstration using Open-Meteo API when OpenWeatherMap API key is missing
            print(f"Notice: OpenWeatherMap returned status {response.status_code}. Using Open-Meteo fallback...")
            fallback_url = "https://api.open-meteo.com/v1/forecast?latitude=23.0225&longitude=72.5714&current_weather=true"
            fb_res = requests.get(fallback_url).json()
            curr = fb_res.get("current_weather", {})
            print(f"=== Weather Report for {city} (Open-Meteo) ===")
            print(f"Temperature : {curr.get('temperature')}°C")
            print(f"Windspeed   : {curr.get('windspeed')} km/h")
    except Exception as e:
        print(f"Error fetching weather: {e}")

if __name__ == "__main__":
    get_weather()
