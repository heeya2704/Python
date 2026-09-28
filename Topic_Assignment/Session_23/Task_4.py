# Build a small script that fetches movies from the OMDB API (http://www.omdbapi.com/) 
# by sending a GET request with query parameters: apikey='demo', s='Avengers'. 
# Print the total number of results found.
# 
# Hint: Pass the parameters using the params={} argument in requests.get().

import requests

url = "http://www.omdbapi.com/"
params = {
    "apikey": "demo",
    "s": "Avengers"
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    if data.get("Response") == "True":
        print(f"Total results found for 'Avengers': {data.get('totalResults')}")
    else:
        print(f"API Response message: {data.get('Error', 'No details available')}")
else:
    print(f"HTTP Request failed with status code: {response.status_code}")
