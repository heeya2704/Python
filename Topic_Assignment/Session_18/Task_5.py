# Download a sample Instagram comments text file (or create your own with at least 10 lines), 
# then write a Python script to extract all valid Instagram usernames (pattern: starts with '@', 
# followed by letters, numbers, underscores, minimum 3 characters) using re.findall() 
# and print the unique usernames.

import re

with open("Session_18/insta_comments.txt", "r") as file:
    content = file.read()

pattern = r'@[a-zA-Z0-9_]{3,}'

usernames = re.findall(pattern, content)
unique_usernames = sorted(list(set(usernames)))

print("Extracted Unique Instagram Usernames:")
for username in unique_usernames:
    print(username)
