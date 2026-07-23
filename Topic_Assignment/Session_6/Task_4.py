# Create two sets: flipkart_users and myntra_users, each containing 5 unique usernames. 
# Find and print the set of users who have accounts on both platforms using set intersection.

flipkart_users = {"heeya", "rahul", "priya", "amit", "neha"}
myntra_users = {"priya", "heeya", "sneha", "rohit", "amit"}

common_users = flipkart_users.intersection(myntra_users)

print("Users on both platforms:")
print(common_users)