import sys
import math
#import statistics
import numpy as np
# import pandas as pd

# def rank(list):
	# return sorted(range(len(list)), key=list.__getitem__)

# def rankdata(a):
    # n = len(a)
    # ivec=rank(a)
    # svec=[a[rank] for rank in ivec]
    # sumranks = 0
    # dupcount = 0
    # newarray = [0]*n
    # for i in range(n):
        # sumranks += i
        # dupcount += 1
        # if i==n-1 or svec[i] != svec[i+1]:
            # averank = sumranks / float(dupcount) + 1
            # for j in range(i-dupcount+1,i+1):
                # newarray[ivec[j]] = averank
            # sumranks = 0
            # dupcount = 0
    # return newarray
# def rank(vector):
    # return [vector.index(x) for x in sorted(range(n-1), key=vector.__getitem__)]
	
# def rank(vector):
      # a={}
      # rank=1
      # for num in sorted(vector):
          # if num not in a:
              # a[num]=rank
              # rank=rank+1
      # return[a[i] for i in vector]
	  
n = int(input('Enter set size:  '))
x = input('Enter X values   ')
y = input('Enter Y values   ')

X = list([float(i) for i in x.split()])
Y = list([float(i) for i in y.split()])

# print(X)
# print(Y)
Xnp = np.asarray(X)
Ynp = np.asarray(Y)
# print(Xnp)
# print(Ynp)

Xt = Xnp.argsort()
Xrank = np.arange(len(Xnp))[Xt.argsort()]
Yt = Ynp.argsort()
Yrank = np.arange(len(Ynp))[Yt.argsort()]
# Xpd = pd.DataFrame(X)
# Ypd = pd.DataFrame(Y)

# Xrank = pd.DataFrame.rank(Xpd)
# Yrank = pd.DataFrame.rank(Ypd)
#print(Xrank)
#print(Yrank)
# print(Xrank[i])
# print(Yrank[i])

sumD = 0 
for i in range(n):
	sumD += (Xrank[i] - Yrank[i])**2
	
	
r = 1 - (6 * sumD)/(n * (n**2 -1))

# # Xmean = sum(X)/float(n)
# # Ymean = sum(Y)/float(n)
# # Xstd = statistics.stdev(X)
# # Ystd = statistics.stdev(Y)

# # print(Xmean)
# # print(Ymean)
# # print(Xstd)
# # print(Ystd)

# # sumXY = 0
# # for i in range(n):
	# # sumXY += (X[i] - Xmean) * (Y[i] - Ymean)

# # pearson = sumXY/(n * Xstd * Ystd)


print("{0:0.3f}".format(r))
