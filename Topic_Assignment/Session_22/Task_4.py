# Modify your GET request to https://jsonplaceholder.typicode.com/posts so it only fetches 
# posts by userId=2 by passing the correct query parameter. Print the IDs of the returned posts.
# 
# Hint: Use the 'params' argument in requests.get().

import requests

url = "https://jsonplaceholder.typicode.com/posts"
params = {"userId": 2}

response = requests.get(url, params=params)

if response.status_code == 200:
    posts = response.json()
    post_ids = [post["id"] for post in posts]
    print(f"Posts fetched for userId=2 (Total: {len(post_ids)}):")
    print("Post IDs:", post_ids)
else:
    print(f"Request failed with status code {response.status_code}")
