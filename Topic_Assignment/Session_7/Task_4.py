# Write a Python program that asks the user to enter their IPL fantasy team points and 
# uses nested if-else statements to print: 'Champion' if points > 800, 'Top Performer' 
# if points between 500 and 800, 'Keep Trying' otherwise.<br><br><em><strong>Hint:</strong> 
# Use nested if-else blocks to check the ranges.</em>

points = int(input("Enter your IPL fantasy team points: "))

if points > 500:
    if points > 800:
        print("Champion")
    else:
        print("Top Performer")
else:
    print("Keep Trying")