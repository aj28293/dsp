import sys
import math


v = input('Enter 1st and 2nd ratios:   ')


V = list([float(i) for i in v.split()])
V1 = V[0]
V2 = V[1]
n = 6
x = 3

p = V1/(V1+V2)
q = 1 - p

# print(p)
# print(q)

b = 0
for i in range(x,n+1):
	nx = (math.factorial(n)/(math.factorial(i)*(math.factorial(n-(i)))))
	b +=  (nx * p**(i) * q**(n-(i)))


print("{0:0.3f}".format(b))