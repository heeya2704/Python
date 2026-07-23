# Write a function get_unique_artists(spotify_playlist1, spotify_playlist2) 
# that takes two sets of artist names and returns a set of all unique artists 
# across both playlists (set union).<br><br><em><strong>Hint:</strong> 
# Use the union() method or the | operator for sets.</em>

def get_unique_artists(spotify_playlist1, spotify_playlist2):
    return spotify_playlist1.union(spotify_playlist2)

playlist1 = {"Arijit Singh", "Shreya Ghoshal", "Atif Aslam"}
playlist2 = {"Arijit Singh", "Neha Kakkar", "Sonu Nigam"}

all_artists = get_unique_artists(playlist1, playlist2)

print("Unique Artists:")
print(all_artists)

# Since sets are unordered, the output order may be different.

# These solutions cover dictionary operations (add, update, delete), 
# filtering dictionary values, set intersection, and set union exactly 
# as required by the assignment.