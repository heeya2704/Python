# Use the datetime module to get the current date and time, 
# then format and print it as 'DD-MM-YYYY HH:MM:SS', similar to how WhatsApp shows message timestamps.
# Hint: Use strftime() to format the output.

from datetime import datetime

current_datetime = datetime.now()
formatted_timestamp = current_datetime.strftime("%d-%m-%Y %H:%M:%S")

print(f"WhatsApp Message Timestamp: {formatted_timestamp}")
