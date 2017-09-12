# Complete the function below.
import csv
import string
import re
#import operator

def count_titles(csv_file_name):
	with open(csv_file_name, 'r') as f:
		faculty = [row for row in csv.reader(f.read().splitlines())]


	titles = faculty[1:]
	titles_col = [[l[i] for i in [2]] for l in titles]

	titles_dict = {'Assistant Professor of Biostatistics': 0, 'Associate Professor of Biostatistics': 0, 'Professor of Biostatistics': 0}
	for count, i in enumerate(titles_col):
		if "Assistant Professor is Biostatistics" in titles_col[count][0]:
			titles_col[count][0] = "Assistant Professor of Biostatistics"

	for count, i in enumerate(titles_col):   
		if "Assistant" in titles_col[count][0]:
			titles_dict['Assistant Professor of Biostatistics'] += 1
		if "Associate" in titles_col[count][0]:
			titles_dict['Associate Professor of Biostatistics'] += 1
		if titles_col[count][0] == "Professor of Biostatistics":
			titles_dict['Professor of Biostatistics'] += 1
        

	print(titles_dict)

count_titles('faculty.csv')
