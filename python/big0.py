import time
import csv
#import pandas as pd

# list1 = pd.read_csv('list1.csv', sep=',',header=None)
# list2 = pd.read_csv('list2.csv', sep=',',header=None)

with open('list1.csv', 'r') as f:
	list1 = [row for row in csv.reader(f.read().splitlines())]
	
with open('list2.csv', 'r') as f:
	list2 = [row for row in csv.reader(f.read().splitlines())]
	
def merge_one(list1, list2):
	start = time.time()
	lists = (sorted(list1 + list2))
	end = time.time()
	totalTime = (end - start) * 1000000
	print("Merge_one: %d" %totalTime)


def merge_two(list1, list2):
	start = time.time()
	l = []
	while list1 and list2:
		if list1[0] < list2[0]:
			l.append(list1.pop(0))
		else:
			l.append(list2.pop(0))
	end = time.time()
	totalTime = (end - start) * 1000000
	print("Merge_two: %d" %totalTime)
	
merge_one(list1, list2)
merge_two(list1, list2)

