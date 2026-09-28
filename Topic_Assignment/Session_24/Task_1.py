# Use the requests library to send a POST request to https://jsonplaceholder.typicode.com/posts 
# with a JSON payload containing a title, body, and userId, then print the response status code and JSON data.

import requests

url = "https://jsonplaceholder.typicode.com/posts"
payload = {
    "title": "Learning Python API Integration",
    "body": "Building automated HTTP client scripts using requests.",
    "userId": 5
}

response = requests.post(url, json=payload)

print(f"Status Code: {response.status_code}")
print("Response JSON:")
print(response.json())
