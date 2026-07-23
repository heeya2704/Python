# Write a lambda function to convert a list of song titles from Spotify to 
# all lowercase letters and use map() to apply it to ['Shape Of You', 
# 'Blinding Lights', 'Levitating', 'Senorita'], printing the cleaned list.

songs = ["Shape Of You", "Blinding Lights", "Levitating", "Senorita"]

lowercase_songs = list(map(lambda song: song.lower(), songs))

print(lowercase_songs)