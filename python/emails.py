# Complete the function below.
import csv
import string
import re
#import operator

def emails(csv_file_name):
	with open(csv_file_name, 'r') as f:
		faculty = [row for row in csv.reader(f.read().splitlines())]


	emails = faculty[1:]
	emails_col = [[l[i] for i in [3]] for l in emails]
	
	email_list =[]
	for count, i in enumerate(emails_col):
		email_list.append(emails_col[count][0])
		
	print(list(email_list))

emails('faculty.csv')
