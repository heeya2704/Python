# Fetch a list of users from https://jsonplaceholder.typicode.com/users using requests.get(), 
# then use the .json() method to extract and print the usernames of all users whose email ends with '.org'.

import requests

url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)

if response.status_code == 200:
    users = response.json()
    print("Usernames of users with email ending in '.org':")
    for user in users:
        email = user.get("email", "")
        if email.endswith(".org"):
            print(f"- Username: {user.get('username')} (Email: {email})")
else:
    print(f"Failed to fetch users. Status code: {response.status_code}")
