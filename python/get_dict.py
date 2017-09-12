import csv
import string
import re

def get_dict():
	with open('faculty.csv', 'r') as f:
		faculty = [row for row in csv.reader(f.read().splitlines())]


	names = faculty[1:]
	names_col = [[l[i] for i in [0]] for l in names]
	keys = []
	values = []
	
	for count, i in enumerate(names_col):
		keys.append((names_col[count][0].split())[-1])
	

	values = [0] * len(keys)
	faculty_dict = dict(zip(keys, values))
	
	for count, i in enumerate(keys):
		for c, j in enumerate(names):
			if i in names[c][0]:
				if faculty_dict[i] == 0:
					faculty_dict[i] = names[c][1:]
				else:
					faculty_dict[i].append(names[c][1:])
	
			
        

	print(faculty_dict)

get_dict()