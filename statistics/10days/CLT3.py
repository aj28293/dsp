import sys
import math
# from sympy import *

# def erf(x, z):
    # return ((2/math.sqrt(math.pi)) * (integrate(exp(-x), (x, 0, z))))

sample = float(input('Enter sample size:  '))
mean = float(input('Enter mean   '))
std = float(input('Enter std   '))
interval = float(input('Enter interval:   '))
z = float(input('Enter z   '))

A = mean - (z*(std/math.sqrt(sample)))
B = mean + (z*(std/math.sqrt(sample)))


print("{0:0.2f}".format(A))
print("{0:0.2f}".format(B))