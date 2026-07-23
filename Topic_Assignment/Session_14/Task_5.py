# Use the pathlib module to check if a file called 'my_fav_apps.json' exists in 
# your current directory, and if not, create it and write a JSON array of your 
# top 3 mobile apps (e.g., Instagram, Zomato, Paytm) with their names and categories.
# <br><br><em><strong>Hint:</strong> Use Path('my_fav_apps.json').exists() to check for the file, 
# and json.dump() to write the data.</em>

from pathlib import Path
import json

file_path = Path("Session_14/my_fav_apps.json")

if not file_path.exists():
    apps = [
        {"name": "Instagram", "category": "Social Media"},
        {"name": "Zomato", "category": "Food Delivery"},
        {"name": "Paytm", "category": "Payments"}
    ]

    with open(file_path, "w") as file:
        json.dump(apps, file, indent=4)

    print("my_fav_apps.json created successfully.")
else:
    print("my_fav_apps.json already exists.")