# Add two more song IDs to your playlist_ids list using both append() 
# and extend(), then print the updated list.<br><br><em><strong>
# Hint:</strong> Use append() for a single ID and extend() for 
# adding multiple IDs at once.</em>

playlist_ids = [101, 102, 103, 104, 105]

# Add one song ID
playlist_ids.append(106)

# Add multiple song IDs
playlist_ids.extend([107, 108])

print("Updated Playlist:", playlist_ids)