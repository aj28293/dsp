import sys



#print('Enter X and N:')
x = input('Enter X   ')
n = input('Enter N   ')

X = float(x)
N = list([int(i) for i in n.split()])
fN = list([float(i) for i in N])
mean = sum(fN)/X
N = sorted(N)
index = int((X -1 )//2)
if X % 2 == 1:
    median = N[index]
else: 
    median = (N[index] + N[index +1])/2.0
mode = int(min([x for x in fN if fN.count(x) == (max([fN.count(a) for a in fN]))]))

print("{0:0.1f}".format(mean))
print("{0:0.1f}".format(median))
print(mode)