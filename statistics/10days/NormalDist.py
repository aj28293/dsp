import sys
import math

# def erf(x, z):
    # return ((2/math.sqrt(math.pi)) * (integrate(exp(-x), (x, 0, z))))

ms = input('Enter mean and std dev:   ')
l = input('Enter less than   ')
between = input('Enter between   ')

MS = list([int(i) for i in ms.split()])
less = float(l)
Between = list([int(i) for i in between.split()])

mean = MS[0]
std = MS[1]
lower = Between[0]
higher = Between[1]

#cdf1 = .5 * (1 + ((less - mean)/(std*math.sqrt(2))))
#cdf2 = 1 - (.5 * (1 + ((lower - mean)/(std*math.sqrt(2)))) + (1 - .5 * (1 + ((higher - mean)/(std*math.sqrt(2))))))
cdf1 = .5 * (1 + math.erf(((less - mean)/(std*math.sqrt(2)))))
cdf2 = 1 - (.5 * (1 + math.erf(((lower - mean)/(std*math.sqrt(2))))) + (1 - .5 * (1 + math.erf(((higher - mean)/(std*math.sqrt(2)))))))


print("{0:0.3f}".format(cdf1))
print("{0:0.3f}".format(cdf2))