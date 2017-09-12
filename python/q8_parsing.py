# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.
import csv

def read_data(filename):
    """Returns a list of lists representing the rows of the csv file data.

    Arguments: filename is the name of a csv file (as a string)
    Returns: list of lists of strings, where every line is split into a list of values. 
        ex: ['Arsenal', 38, 26, 9, 3, 79, 36, 87]
    """
    with open(filename, 'r') as f:
        footballTable = [row for row in csv.reader(f.read().splitlines())]
    
    #footballTable = []
    #for count, i in enumerate(football):
     #   footballTable[count]
    return footballTable


def get_index_with_min_abs_score_difference(goals):
    """Returns the index of the team with the smallest difference
    between 'for' and 'against' goals, in terms of absolute value.

    Arguments: parsed_data is a list of lists of cleaned strings
    Returns: integer row index
    """
    #3goals['gd'] = 0
    #for i in goals:
     #   goals['gd'][i] = goals['Goals'][i] - goals['Goals Allowed'][i]
    
    goalsMade = [x[5] for x in goals[1:]]
    goalsAllowed = [x[6] for x in goals[1:]]
    stats = zip(goalsMade, goalsAllowed)
    goalsDiff = [float(i) - float(j) for i, j in stats]
    
    return goalsDiff.index(min(goalsDiff))
    
    
def get_team(index_value, parsed_data):
    """Returns the team name at a given index.
    
    Arguments: index_value is an integer row index
               parsed_data is the output of `read_data` above
               
    Returns: the team name
    """
    teamNames = [i[0] for i in parsed_data[1:]]
    return teamNames[index_value]

footballTable = read_data('football.csv')
minRow = get_index_with_min_abs_score_difference(footballTable)
print(str(get_team(minRow, footballTable)))