# Define a Python class called Song with attributes title, artist, 
# and duration (in seconds). Create an object for your favorite song and print its details.

class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

# Example usage:
fav_song = Song("Shape Of You", "Ed Sheeran", 233)

print("Song Details:")
print("Title:", fav_song.title)
print("Artist:", fav_song.artist)
print("Duration:", fav_song.duration, "seconds")
