# Complete the function below.
import csv
import string
import re
#import operator

def get_dict(csv_file_name):
	with open(csv_file_name, 'r') as f:
		faculty = [row for row in csv.reader(f.read().splitlines())]


	degrees = faculty[1:]
	degrees_col = [[l[i] for i in [1]] for l in degrees]
	keys1 = []
	keys2 = []
	keys = []
	values = []
	
	for count, i in enumerate(degrees_col):
		degrees_col[count][0] = str(re.sub('[.]', '', degrees_col[count][0]))
		
	for count, i in enumerate(degrees_col):
		keys1.append(str(degrees_col[count][0].split()))
		
	# keys2 = [item for list1 in keys1 for item in list1]		
	# for count, i in enumerate(keys1):
		# keys1[count][0] = re.sub('["[]'"]', '', keys1[count][0])
	
	for count, i in enumerate(keys1):
		for c, j in enumerate(keys1[count]):
			keys.append(keys1[count][c].split())
	
	
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

get_dict('faculty.csv')
