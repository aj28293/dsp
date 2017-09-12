import sys
import math
# from sympy import *

# def erf(x, z):
    # return ((2/math.sqrt(math.pi)) * (integrate(exp(-x), (x, 0, z))))

max = float(input('Enter max:  '))
boxes = float(input('Enter number:   '))
mean = float(input('Enter mean   '))
std = float(input('Enter mean   '))

cdf1 = .5 * (1 + math.erf((max - (boxes * mean))/((std*math.sqrt(boxes))*math.sqrt(2))))


print("{0:0.4f}".format(cdf1))
