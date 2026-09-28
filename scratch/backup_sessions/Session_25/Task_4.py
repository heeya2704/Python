# Many APIs require Bearer tokens for authentication. Write a function get_user_profile() 
# that calls a mock API endpoint (e.g., https://jsonplaceholder.typicode.com/users/1) 
# using a fake Bearer token in the Authorization header, and prints the user's name.
# 
# Constraint: Use the 'Authorization: Bearer <token>' header format.

import requests

def get_user_profile(user_id=1, token="fake_bearer_token_xyz987"):
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        user_data = response.json()
        print(f"Header Passed : Authorization: Bearer {token}")
        print(f"User Name     : {user_data.get('name')}")
        print(f"User Email    : {user_data.get('email')}")
        print(f"Company       : {user_data.get('company', {}).get('name')}")
    else:
        print(f"Request failed with status code: {response.status_code}")

if __name__ == "__main__":
    get_user_profile()
