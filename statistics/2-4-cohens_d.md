[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

Using the variable totalwgt_lb, investigate whether first babies are lighter or heavier than others.   
Compute Cohen’s effect size to quantify the difference between the groups. How does it compare to the difference in pregnancy length?   

firsts.totalwgt_lb.mean(), others.totalwgt_lb.mean()    
'''First borns appear to be slightly lighter on average than other babies'''   

CohenEffectSize(firsts.totalwgt_lb, others.totalwgt_lb)    
-0.088672927072602006    

'''prglngth = 0.028879044654449883      
totalwgt_lb = -0.088672927072602006    
In both cases the difference in means are both small with 0.029 and -0.89 std deviations respectively,    
depending on the situation may be considered insignificant differences.'''    

