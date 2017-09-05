[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

Exercise: In the BRFSS (see Section 5.4), the distribution of heights is roughly normal with parameters µ = 178 cm and σ = 7.7 cm for men, and µ = 163 cm and σ = 7.3 cm for women.    
In order to join Blue Man Group, you have to be male between 5’10” and 6’1” (see http://bluemancasting.com). What percentage of the U.S. male population is in this range? Hint: use scipy.stats.norm.cdf.    
    
    
import scipy.stats   

mu = 178    
sigma = 7.7   
dist = scipy.stats.norm(loc=mu, scale=sigma)   
type(dist)   

dist.mean(), dist.std()    

dist.cdf(mu-sigma)    

low = 177.8   
high = 185.4  
low_cdf = dist.cdf(low)  
high_cdf = dist.cdf(high)   
high_cdf - low_cdf    

0.34209468294595308 or 34.2% of the population on males are in this distribution





