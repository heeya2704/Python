# Add a method play_preview(self) to the Song class that prints 
# 'Playing 30-second preview of [title] by [artist]'. Call this method using the object you created.

class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

    def play_preview(self):
        print(f"Playing 30-second preview of {self.title} by {self.artist}")

# Example usage:
fav_song = Song("Blinding Lights", "The Weeknd", 200)
fav_song.play_preview()
