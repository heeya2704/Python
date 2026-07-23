# Find a public JSON file of trending movies (or create your own movies.json with 
# at least 3 movie objects containing title, year, and rating), then use the json module 
# in Python to load the file and print the title and rating of each movie.

import json

with open("Session_14/movies.json", "r") as file:
    movies = json.load(file)

for movie in movies:
    print("Title:", movie["title"])
    print("Rating:", movie["rating"])