# Write a short Python script that takes a scenario (like a list of recent 
# Zomato orders vs a tuple of fixed IPL team names) and prints which 
# one should use a list and which should use a tuple,
# explaining your choice in a comment.

# A list is used for recent Zomato orders because orders can be added or removed.
recent_zomato_orders = ["Pizza", "Burger", "Pasta"]

# A tuple is used for IPL team names because they are fixed and do not change.
ipl_team_names = (
    "Chennai Super Kings",
    "Mumbai Indians",
    "Royal Challengers Bengaluru",
    "Kolkata Knight Riders"
)

print("Recent Zomato Orders (List):", recent_zomato_orders)
print("IPL Team Names (Tuple):", ipl_team_names)

# this solution is correct because it clearly explains the reasoning behind using a list for recent orders 
# (which can change) and a tuple for IPL team names (which are fixed).