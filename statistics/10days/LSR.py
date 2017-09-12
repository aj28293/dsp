import sys
import math

def linear_regression(x, y):
    
    length = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    
    sum_x_squared = sum(map(lambda a: a * a, x))
    sum_of_products = sum([x[i] * y[i] for i in range(length)])

    a = (sum_of_products - (sum_x * sum_y) / length) / (sum_x_squared - ((sum_x ** 2) / length))
    b = (sum_y - a * sum_x) / length
    return a, b
	  
s1 = input('Enter student score:  ')
s2 = input('Enter student score:  ')
s3 = input('Enter student score:  ')
s4 = input('Enter student score:  ')
s5 = input('Enter student score:  ')

S1 = list([float(i) for i in s1.split()])
S2 = list([float(i) for i in s2.split()])
S3 = list([float(i) for i in s3.split()])
S4 = list([float(i) for i in s4.split()])
S5 = list([float(i) for i in s5.split()])

X = [0, 0, 0, 0, 0]
Y = [0, 0, 0, 0, 0]

X[0] = S1[0]
X[1] = S2[0]
X[2] = S3[0]
X[3] = S4[0]
X[4] = S5[0]
Y[0] = S1[1]
Y[1] = S2[1]
Y[2] = S3[1]
Y[3] = S4[1]
Y[4] = S5[1]

lrl = linear_regression(X, Y)

x = 80
y = lrl[1] + x*lrl[0]


print("{0:0.3f}".format(y))
