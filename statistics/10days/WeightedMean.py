import sys



#print('Enter X and N:')
x = input('Enter X   ')
n = input('Enter N   ')
w = input('Enter W   ')

X = float(x)
N = list([float(i) for i in n.split()])
W = list([float(i) for i in w.split()])
#fN = list([float(i) for i in N])
weightedN = []
for c, i in enumerate(N):
	weightedN.append(N[c] * W[c])
	
mean = sum(weightedN)/sum(W)


print("{0:0.1f}".format(mean))
