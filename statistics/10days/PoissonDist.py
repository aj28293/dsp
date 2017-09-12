import sys
import math


#print('Enter X and N:')
l = input('Enter lambda   ')
k = input('Enter k   ')
# w = input('Enter W   ')

L = float(l)
K = int(k)
# x = 1

# p = X[0]/X[1]
# q = 1 - p


poisson = ((L**K)*math.exp(-L))/(math.factorial(K))





print("{0:0.3f}".format(poisson))
