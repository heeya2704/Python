# Send a POST request to https://jsonplaceholder.typicode.com/posts to add a new playlist 
# with fields: title, userId, and body. Print the status code and the JSON response.
# 
# Hint: Use requests.post() and pass your data as a JSON payload.

import requests

url = "https://jsonplaceholder.typicode.com/posts"

payload = {
    "title": "My Favorite Hits 2026",
    "userId": 1,
    "body": "A curated list of top pop and rock tracks for coding sessions."
}

response = requests.post(url, json=payload)

print(f"Status Code: {response.status_code}")
print("JSON Response:")
print(response.json())
