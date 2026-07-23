# Write a Python function that takes a list of IPL team names and 
# prints only those teams whose names are longer than 6 characters, 
# skipping the rest using the continue statement.

def print_long_team_names(teams):
    for team in teams:
        if len(team) <= 6:
            continue
        print(team)

ipl_teams = [
    "CSK",
    "Mumbai Indians",
    "RCB",
    "Kolkata Knight Riders",
    "Gujarat Titans",
    "LSG"
]

print_long_team_names(ipl_teams)