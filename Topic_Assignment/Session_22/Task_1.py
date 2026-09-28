# Use the requests library in Python to send a GET request to the public API 
# https://jsonplaceholder.typicode.com/posts and print the titles of the first 5 posts.

import requests

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)

if response.status_code == 200:
    posts = response.json()
    print("Titles of the first 5 posts:")
    for index, post in enumerate(posts[:5], start=1):
        print(f"{index}. {post['title']}")
else:
    print(f"Failed to fetch posts. Status code: {response.status_code}")
