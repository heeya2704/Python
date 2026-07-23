# Download a sample CSV file of IPL match scores (you can create your own with 
# columns: match_id, team1, team2, winner) and write a Python script to read the file and 
# print the winner of each match using the csv module.

import csv

with open("Session_14/ipl_matches.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print("Winner:", row["winner"])