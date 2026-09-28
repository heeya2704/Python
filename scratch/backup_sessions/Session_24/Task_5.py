# Modify your script to save the same API data (latest 5 posts from 
# https://jsonplaceholder.typicode.com/posts) into a JSON file named posts.json instead of CSV.

import requests
import json
import os

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)

if response.status_code == 200:
    posts = response.json()[:5]
    
    extracted_data = [
        {"userId": post["userId"], "title": post["title"]}
        for post in posts
    ]
    
    file_path = os.path.join(os.path.dirname(__file__), "posts.json")
    with open(file_path, "w", encoding="utf-8") as json_file:
        json.dump(extracted_data, json_file, indent=4)
        
    print(f"Successfully saved 5 posts to '{file_path}'")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
