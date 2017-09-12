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
f = input('Enter F   ')

X = int(x)
N = list([int(i) for i in n.split()])
F = list([int(i) for i in f.split()])
#fN = list([float(i) for i in N])
extN = []
for c in range(len(N)):
	for i in range(F[c]):
		extN.append(N[c])

extN = sorted(extN)

mid = int(len(extN)/2)
#Q2 = median(extN)

if len(extN) % 2 == 0:
	Q1 = median(extN[:mid])
	Q3 = median(extN[mid:])
else:
	Q1 = median(extN[:mid])
	Q3 = median(extN[mid+1:])

print("{0:0.1f}".format(float(Q3) - float(Q1)))