# Use the NASA Astronomy Picture of the Day (APOD) API to get today's image title and 
# explanation, and save the image to your local system.
# 
# Hint: The API returns a URL for the image — use requests to download it.

import requests
import os

url = "https://api.nasa.gov/planetary/apod"
params = {
    "api_key": "DEMO_KEY"
}

try:
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        title = data.get("title")
        explanation = data.get("explanation")
        media_type = data.get("media_type")
        image_url = data.get("url")
        
        print(f"Title: {title}\n")
        print(f"Explanation:\n{explanation}\n")
        
        if media_type == "image":
            img_res = requests.get(image_url)
            if img_res.status_code == 200:
                filename = os.path.join(os.path.dirname(__file__), "apod_today.jpg")
                with open(filename, "wb") as f:
                    f.write(img_res.content)
                print(f"Image saved successfully to: '{filename}'")
        else:
            print(f"Today's media is a {media_type}: {image_url}")
    else:
        print(f"Failed to fetch NASA APOD data. Status code: {response.status_code}")
except Exception as e:
    print(f"Error fetching NASA APOD: {e}")
