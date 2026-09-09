# Write a Python function called get_song_duration_per_minute that divides the 
# total duration of a Spotify playlist (in minutes) by the number of songs, and 
# handles the case where the number of songs is zero using try, except, and finally blocks.

def get_song_duration_per_minute(total_duration, num_songs):
    try:
        if num_songs == 0:
            raise ValueError("Number of songs cannot be zero.")
        return total_duration / num_songs
    except ValueError as e:
        print(f"Error: {e}")
        return None
    finally:
        print("Calculation completed.")
        
# Example usage:
total_duration = 120  # total duration in minutes
num_songs = 0  # number of songs
average_duration = get_song_duration_per_minute(total_duration, num_songs)