import sys
import math


#print('Enter X and N:')
l1 = input('Enter lambda1   ')
l2 = input('Enter lambda2   ')
# w = input('Enter W   ')

L1 = float(l1)
L2 = float(l2)

Ca = 160 + (40*(L1 + L1**2))
Cb = 128 + (40*(L2 + L2**2))




print("{0:0.3f}".format(Ca))
print("{0:0.3f}".format(Cb))