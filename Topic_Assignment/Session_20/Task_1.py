# Create a Python class called Playlist with a private attribute _songs (a list) 
# and a public method add_song(song) to add a song title to the playlist. 
# Print the playlist after adding 3 songs.

class Playlist:
    def __init__(self):
        self._songs = []

    def add_song(self, song):
        self._songs.append(song)
        print(f"Added '{song}' to playlist.")

    def display_playlist(self):
        print("Playlist Songs:", self._songs)

# Example usage:
my_playlist = Playlist()
my_playlist.add_song("Shape Of You")
my_playlist.add_song("Blinding Lights")
my_playlist.add_song("Levitating")

my_playlist.display_playlist()
