import sys
import math
# from sympy import *

# def erf(x, z):
    # return ((2/math.sqrt(math.pi)) * (integrate(exp(-x), (x, 0, z))))

max = float(input('Enter tickets left:  '))
students = float(input('Enter number of students:   '))
mean = float(input('Enter mean   '))
std = float(input('Enter std   '))

cdf1 = .5 * (1 + math.erf((max - (students * mean))/((std*math.sqrt(students))*math.sqrt(2))))


print("{0:0.4f}".format(cdf1))
