import sys
import math
#from sklearn import linear_model
import numpy as np

def MLR(X, y, merror, ):  
    temp = np.matrix(np.zeros(theta.shape))
    parameters = int(theta.ravel().shape[1])
    cost = np.zeros(iters)

    for i in range(iters):
        error = (X * theta.T) - y

        for j in range(parameters):
            term = np.multiply(error, X[:,j])
            temp[0,j] = theta[0,j] - ((alpha / len(X)) * np.sum(term))

        theta = temp
        cost[i] = computeCost(X, y, theta)

    return theta, cost
	  
s1 = input('Enter observed and # of feature sets ')
S1 = list([int(i) for i in s1.split()])
m = S1[0]
n = S1[1]

S2 = []
for t in range(0,S1[1]):
	S2.append(list([float(i) for i in input('Enter features:   ').split()]))

X=[]
Y=[]
j = (len(S2[0]) - 1)

for i in range(0,n):	
	
	X.append(S2[i][0:j])
	Y.append(S2[i][-1])

# print(X,Y)	

q = int(input('Enter number of feature sets:   '))

S4 = []
for t in range(0,q):
	S4.append(list([float(i) for i in input('Enter features:   ').split()]))

lm = linear_model.LinearRegression()
lm.fit(X, Y)
a = lm.intercept_
b = lm.coef_
print (a, b )

Y_forecast = []
for i in range(0,q):
	print("{0:0.2f}".format(a + S4[i][0] * b[0] + S4[i][1] * b[1]))

	
#print(m, n, S2, q, S4)


#print("{0:0.3f}".format(y))
