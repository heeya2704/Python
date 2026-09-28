# Send a POST request to https://reqres.in/api/users with a JSON object containing 
# a username and job, then parse the response to extract and print the created user's ID 
# and creation timestamp.
# 
# Hint: Use response.json() to access the returned data.

import requests

url = "https://reqres.in/api/users"
payload = {
    "name": "morpheus",
    "job": "leader"
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

try:
    response = requests.post(url, json=payload, headers=headers, timeout=10)
    print(f"Status Code: {response.status_code}")
    if response.status_code in (200, 201):
        data = response.json()
        print(f"Created User ID           : {data.get('id')}")
        print(f"Creation Timestamp (createdAt): {data.get('createdAt')}")
    else:
        print(f"Response Body: {response.text}")
except Exception as e:
    print(f"An error occurred: {e}")
