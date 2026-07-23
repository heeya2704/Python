# You have a list of song durations (in seconds) from your Spotify playlist. 
# Use a for loop with enumerate to print each song's position (starting from 1) 
# and its duration in the format: 'Song 1: 210 seconds'.

song_durations = [210, 185, 240, 195, 220]

for position, duration in enumerate(song_durations, start=1):
    print(f"Song {position}: {duration} seconds")