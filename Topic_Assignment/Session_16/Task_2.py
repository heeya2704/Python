# Write a generator function called playlist_generator that takes a list of 
# song names and yields each song one at a time, simulating a Spotify playlist shuffle.

def playlist_generator(songs):
    for song in songs:
        yield song

# Example usage:
songs_list = ["Shape Of You", "Blinding Lights", "Levitating", "Senorita", "Starboy"]
spotify_playlist = playlist_generator(songs_list)

print("Spotify Playlist Shuffle:")
for song in spotify_playlist:
    print(f"Now Playing: {song}")
