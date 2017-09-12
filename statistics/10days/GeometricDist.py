import sys



#print('Enter X and N:')
x = input('Enter X   ')
n = input('Enter N   ')
# w = input('Enter W   ')

N = int(n)
X = list([float(i) for i in x.split()])
# W = list([float(i) for i in w.split()])
#fN = list([float(i) for i in N])

p = X[0]/X[1]
q = 1 - p



# weightedN = []
# for c, i in enumerate(N):
	# weightedN.append(N[c] * W[c])
	
# mean = sum(weightedN)/sum(W)


print("{0:0.3f}".format(float(q**(N-1) * p)))
