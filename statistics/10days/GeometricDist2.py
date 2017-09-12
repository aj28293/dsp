import sys
import math


#print('Enter X and N:')
x = input('Enter X   ')
n = input('Enter N   ')
# w = input('Enter W   ')

N = int(n)
X = list([float(i) for i in x.split()])
x = 1

p = X[0]/X[1]
q = 1 - p


prob = (p**x * q**(N-x) * (math.factorial(N)/(math.factorial(x)*math.factorial(N-x))))





print("{0:0.3f}".format(prob))
