# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

import numpy as np
import csv
def main():
    with open("football.csv", "r") as csvfile2:
        reader = csv.reader(csvfile2)
        goals_for = []
        goals_against = []
        goals_diff = []
        teams = []
        next(reader)
        for x in reader:
          goals_for.append(x[5])
          goals_against.append(x[6])
          teams.append(x[0])
        for x,y in zip(goals_for, goals_against):
          goals_diff.append(abs(int(x)-int(y)))
          index = np.array(goals_diff).argmin()
        print(teams[index])
    
if __name__ == "__main__":
    main()
