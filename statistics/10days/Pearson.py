import sys
import math
import statistics


n = int(input('Enter set size:  '))
x = input('Enter X values   ')
y = input('Enter Y values   ')

X = list([float(i) for i in x.split()])
Y = list([float(i) for i in y.split()])

Xmean = sum(X)/float(n)
Ymean = sum(Y)/float(n)
Xstd = statistics.stdev(X)
Ystd = statistics.stdev(Y)

print(Xmean)
print(Ymean)
print(Xstd)
print(Ystd)

sumXY = 0
for i in range(n):
	sumXY += (X[i] - Xmean) * (Y[i] - Ymean)

pearson = sumXY/(n * Xstd * Ystd)


print("{0:0.3f}".format(pearson))
