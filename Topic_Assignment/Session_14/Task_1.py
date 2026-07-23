# Create a text file named playlist.txt and write the names of 5 songs 
# you listened to this week, each on a new line using Python's open() function in write mode.

songs = [
    "Shape Of You",
    "Blinding Lights",
    "Levitating",
    "Senorita",
    "Perfect"
]

with open("Session_14/playlist.txt", "w") as file:
    for song in songs:
        file.write(song + "\n")

print("playlist.txt created successfully.")