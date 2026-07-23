# Given a list of Zomato restaurant ratings [4.2, 3.8, 4.5, 2.9, 3.5], 
# use filter() with a lambda to find and print only the restaurants with ratings above 4.0.

ratings = [4.2, 3.8, 4.5, 2.9, 3.5]

high_ratings = list(filter(lambda rating: rating > 4.0, ratings))

print(high_ratings)