# Build a Python script that lets a user enter a new playlist name and description, 
# sends this data as JSON in a POST request to a mock API endpoint (such as 
# https://jsonplaceholder.typicode.com/posts), and prints the playlist ID returned by the API.

import requests

def create_playlist(name, description):
    url = "https://jsonplaceholder.typicode.com/posts"
    payload = {
        "title": name,
        "body": description,
        "userId": 1
    }
    
    response = requests.post(url, json=payload)
    if response.status_code in (200, 201):
        data = response.json()
        print(f"\nPlaylist created successfully!")
        print(f"Playlist ID   : {data.get('id')}")
        print(f"Playlist Name : {data.get('title')}")
        print(f"Description   : {data.get('body')}")
    else:
        print(f"Failed to create playlist. Status Code: {response.status_code}")

if __name__ == "__main__":
    name = "Chill Beats 2026"
    desc = "Relaxing lofi tracks for studying and coding."
    print(f"Creating Playlist: '{name}'...")
    create_playlist(name, desc)
