# Use iter() and next() to manually loop through a list of your 5 favorite 
# food delivery apps (like Zomato, Swiggy, Domino's, etc.) and print each app name one by one.

food_apps = ["Zomato", "Swiggy", "Domino's", "Eatsure", "Blinkit"]

app_iterator = iter(food_apps)

print("Favorite Food Delivery Apps:")
print(next(app_iterator))
print(next(app_iterator))
print(next(app_iterator))
print(next(app_iterator))
print(next(app_iterator))
