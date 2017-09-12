import sys
import math
# from sympy import *

# def erf(x, z):
    # return ((2/math.sqrt(math.pi)) * (integrate(exp(-x), (x, 0, z))))

ms = input('Enter mean and std dev:   ')
n1 = input('Enter grade   ')
n2 = input('Enter grade   ')

MS = list([int(i) for i in ms.split()])
N1 = float(n1)
N2 = float(n2)

mean = MS[0]
std = MS[1]



cdf1 =  100 * (1 - (.5 * (1 + math.erf(((N1 - mean)/(std*math.sqrt(2)))))))
cdf2 =  100 * (1 - (.5 * (1 + math.erf(((N2 - mean)/(std*math.sqrt(2)))))))
cdf3 =  100 * ((.5 * (1 + math.erf(((N2 - mean)/(std*math.sqrt(2)))))))


print("{0:0.2f}".format(cdf1))
print("{0:0.2f}".format(cdf2))
print("{0:0.2f}".format(cdf3))