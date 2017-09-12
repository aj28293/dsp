import sys

def median(I):
	J = len(I)
	index = int((J - 1)//2)
	if J % 2 == 1:
		median = I[index]
		return median
	else: 
		median = (I[index] + I[index +1])/2.0
		return median

#print('Enter X and N:')
x = input('Enter X   ')
n = input('Enter N   ')
# w = input('Enter W   ')

X = int(x)
N = list([int(i) for i in n.split()])
# W = list([float(i) for i in w.split()])
#fN = list([float(i) for i in N])
# weightedN = []
N = sorted(N)

mid = int(len(N)/2)
Q2 = median(N)

if len(N) % 2 == 0:
	Q1 = median(N[:mid])
	Q3 = median(N[mid:])
else:
	Q1 = median(N[:mid])
	Q3 = median(N[mid+1:])

print(int(Q1))
print(int(Q2))
print(int(Q3))