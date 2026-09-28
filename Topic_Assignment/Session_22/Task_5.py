# Research using ChatGPT or Copilot to find out how to set custom HTTP headers 
# (like 'Authorization') in a Python requests call. Write a short code snippet that sends 
# a GET request to any API endpoint with a custom header and print the response status code.

import requests

url = "https://jsonplaceholder.typicode.com/posts"

# Setting custom HTTP headers using the 'headers' parameter in requests
headers = {
    "Authorization": "Bearer fake_token_abc123xyz",
    "User-Agent": "MyCustomPythonApp/1.0",
    "Accept": "application/json"
}

response = requests.get(url, headers=headers)

print(f"Request Sent to: {url}")
print(f"Custom Headers Passed: {headers}")
print(f"Response Status Code: {response.status_code}")
