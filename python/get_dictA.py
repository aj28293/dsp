# Complete the function below.
# Complete the function below.
import csv
import string
import re
#import operator

def count_degrees(csv_file_name):
    with open(csv_file_name, 'r') as f:
        faculty = [row for row in csv.reader(f.read().splitlines())]


    degrees = faculty[1:]
    degree_col = [[l[i] for i in [1]] for l in degrees]

    degree_dict = {'PhD': 0, 'ScD': 0, 'MD': 0, 'JD': 0, 'MA' : 0, "MS" : 0, 'BSEd': 0, 'MPH': 0 }
    for count, i in enumerate(degree_col):
        degree_col[count][0] = re.sub('[.]', '', degree_col[count][0])
    for count, i in enumerate(degree_col):   
        if "PhD" in degree_col[count][0]:
            degree_dict['PhD'] += 1
        if "ScD" in degree_col[count][0]:
            degree_dict['ScD'] += 1
        if "MD" in degree_col[count][0]:
            degree_dict['MD'] += 1
        if "JD" in degree_col[count][0]:
            degree_dict['JD'] += 1
        if "MA" in degree_col[count][0]:
            degree_dict['MA'] += 1
        if "MS" in degree_col[count][0]:
            degree_dict['MS'] += 1
        if "BSEd" in degree_col[count][0]:
            degree_dict['BSEd'] += 1
        if "MPH" in degree_col[count][0]:
            degree_dict['MPH'] += 1 

	print(faculty_dict)

get_dict('faculty.csv')
