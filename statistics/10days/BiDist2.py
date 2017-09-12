import sys
import math


v = input('Enter 1st and 2nd ratios:   ')


V = list([float(i) for i in v.split()])
reject_p = V[0]/100
batch = int(V[1])

x = 2

# p = V1/(V1+V2)
q = 1 - reject_p

# print(p)
# print(q)

at_least = 0
for i in range(x,batch+1):
	nx = (math.factorial(batch)/(math.factorial(i)*(math.factorial(batch-(i)))))
	at_least +=  (nx * reject_p**(i) * q**(batch-(i)))

less_than = 0
for i in range(0,X+1):
	nx = (math.factorial(batch)/(math.factorial(i)*(math.factorial(batch-(i)))))
	less_than +=  (nx * reject_p**(i) * q**(batch-(i)))



print("{0:0.3f}".format(less_than))
print("{0:0.3f}".format(at_least))