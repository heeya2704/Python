# Create a custom Python module called playlist_utils.py with a function 
# add_song(playlist, song) that adds a song to a list. Import this module in another 
# script and use it to add three songs to a playlist, then print the final playlist.

import playlist_utils

my_playlist = []

playlist_utils.add_song(my_playlist, "Shape Of You")
playlist_utils.add_song(my_playlist, "Blinding Lights")
playlist_utils.add_song(my_playlist, "Levitating")

print("Final Playlist:")
print(my_playlist)
