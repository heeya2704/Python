# Mini project :  
# Problem Statement : Password Generator  
# Make a program to generate a strong password using the input given by the user. To generate a password, 
# randomly take some words from the user input and then include numbers, special characters and capital 
# letters to generate the password. Also, keep a check that password length is more than 8 characters.   
# Note: Include Exception handling wherever required. Also, make a ‘User’ class and store the details like user 
# id, name and password of each user as a tuple.   

import random
import string

class User:
    def __init__(self, user_id, name, password):
        self.details = (user_id, name, password)

def generate_password(words):
    try:
        if len(words) == 0:
            raise ValueError("No words provided!")

        base = "".join(random.sample(words, min(2, len(words))))

        chars = string.ascii_uppercase + string.digits + "@#$%&*"
        extra = "".join(random.choices(chars, k=6))

        password = base + extra

        if len(password) < 8:
            raise Exception("Password too short!")

        return password

    except Exception as e:
        print("Error:", e)

user_id = int(input("Enter User ID: "))
name = input("Enter Name: ")

words = input("Enter some words: ").split()

password = generate_password(words)

user = User(user_id, name, password)

print("Generated Password:", password)
print("User Details Stored:", user.details)