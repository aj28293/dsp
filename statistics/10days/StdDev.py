import sys
import math

#print('Enter X and N:')
x = input('Enter X   ')
n = input('Enter N   ')

X = float(x)
N = list([float(i) for i in n.split()])
#fN = list([float(i) for i in N])
mean = sum(N)/X
N = sorted(N)

std = math.sqrt(sum([(i - mean)**2 for i in N])/X)

print("{0:0.1f}".format(std))
# print("{0:0.1f}".format(median))
# print(mode)