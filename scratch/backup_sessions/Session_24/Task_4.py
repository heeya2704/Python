# Write a script that fetches the latest 5 posts from https://jsonplaceholder.typicode.com/posts, 
# parses the JSON response, and saves the post titles and userIds to a CSV file called posts.csv.
# 
# Hint: Use the csv module for writing to CSV.

import requests
import csv
import os

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)

if response.status_code == 200:
    posts = response.json()[:5]
    file_path = os.path.join(os.path.dirname(__file__), "posts.csv")
    
    with open(file_path, mode="w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["userId", "title"])
        
        for post in posts:
            writer.writerow([post["userId"], post["title"]])
            
    print(f"Successfully saved 5 posts to '{file_path}'")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
