# Given a list of daily step counts for a week, use a while loop to find and 
# print the first day when you crossed 10,000 steps.<br><br><em><strong>Hint:</strong> 
# Loop through the list and stop as soon as you find a value greater than 10,000.</em>

steps = [7500, 8200, 9800, 10500, 12000, 9500, 11000]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

i = 0

while i < len(steps):
    if steps[i] > 10000:
        print("First day with more than 10,000 steps:", days[i])
        break
    i += 1