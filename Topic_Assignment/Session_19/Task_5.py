# Refactor your Song class so that the duration attribute is optional in 
# the constructor (default to 0 if not provided).
# Hint: Use a default argument for duration in the __init__() method.

class Song:
    def __init__(self, title, artist, duration=0):
        self.title = title
        self.artist = artist
        self.duration = duration

# Example usage:
song1 = Song("Levitating", "Dua Lipa", 203)
song2 = Song("Senorita", "Shawn Mendes & Camila Cabello")

print("Song 1 (duration provided):", song1.title, "-", song1.duration, "s")
print("Song 2 (duration omitted):", song2.title, "-", song2.duration, "s")
