# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import math
#from sympy import *

#def erf(x, z):
  #  return ((2/math.sqrt(math.pi)) * (integrate(exp(-x), (x, 0, z))))

MS = list([int(i) for i in input().split()])
less = float(input())
Between = list([int(i) for i in input().split()])

mean = MS[0]
std = MS[1]
lower = Between[0]
higher = Between[1]

#cdf1 = .5 * (1 + ((less - mean)/(std*math.sqrt(2))))
#cdf2 = 1 - (.5 * (1 + ((lower - mean)/(std*math.sqrt(2)))) + (1 - .5 * (1 + ((higher - mean)/(std*math.sqrt(2))))))
cdf1 = .5 * (1 + math.erf(less,((less - mean)/(std*math.sqrt(2)))))
cdf2 = 1 - (.5 * (1 + math.erf(lower,((lower - mean)/(std*math.sqrt(2))))) + (1 - .5 * (1 + math.erf(higher,((higher - mean)/(std*math.sqrt(2)))))))

print("{0:0.3f}".format(cdf1))
print("{0:0.3f}".format(cdf2))