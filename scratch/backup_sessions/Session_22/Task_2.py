# Create a Python dictionary that represents a Zomato-style restaurant object with fields 
# like name, location, cuisines, and ratings. Convert this dictionary to a JSON string 
# using the json module and print the result.

import json

restaurant = {
    "id": 101,
    "name": "Barbeque Nation",
    "location": "CG Road, Ahmedabad",
    "cuisines": ["North Indian", "BBQ", "Kebabs", "Desserts"],
    "ratings": {
        "aggregate_rating": 4.5,
        "rating_text": "Excellent",
        "votes": 1250
    },
    "is_delivering_now": True,
    "average_cost_for_two": 1500
}

json_string = json.dumps(restaurant, indent=4)
print("Restaurant JSON String:")
print(json_string)
