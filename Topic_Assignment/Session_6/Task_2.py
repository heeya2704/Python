# Add a new influencer to your insta_followers dictionary and 
# update the follower count for one existing influencer. 
# Then, delete one influencer from the dictionary and print the updated dictionary.

insta_followers = {
    "viratkohli": 270000000,
    "shraddhakapoor": 95000000,
    "aliaabhatt": 87000000,
    "deepikapadukone": 80000000,
    "narendramodi": 108000000
}

# Add a new influencer
insta_followers["kiaraaliaadvani"] = 35000000

# Update follower count
insta_followers["aliaabhatt"] = 88000000

# Delete an influencer
del insta_followers["deepikapadukone"]

print("Updated Dictionary:")
print(insta_followers)