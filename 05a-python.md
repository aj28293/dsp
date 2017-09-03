# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

Lists and Tuples are the same except that tuples are immutable.  Lists are a series of objects that can be used for keys in a dictionary.  Given a dictionary is mutable, the keys should be mutable which would require a list not a tuple.  



### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why? 

Sets are lists with only unique values (no duplicates) and unordered.  Sets are faster for look up as the search uses hash lookup.    

listA = [1,1,2,2,3,3,4,5]    
setA = set(listA)    
setB = {1,1,2,2,3,3,4,5}    

print(setA)    
{1, 2, 3, 4, 5}    
   
print(setB)    
{1, 2, 3, 4, 5}    

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

Python lambda is used for inline or anonymous function to be applied rather than creating a whole new function and calling the function.  Usually good when the function will not be reused, ie. one-time use.    

Example:   

cars = [   
    {"type": "Porsche", "doors": 2, "color": "black"},    
    {"type": "BMW", "doors": 4, "color": "blue"},
    {"type": "Ferrari", "doors": 2, "color": "red"}]
    
sorted(cars, key=lambda car: car['doors'])



### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

List Comprehension is a way of transforming one list into another using some filter or map mechanism in one line.     

Examples:   
listA = range(1,11)
listOdds = return_odd = [n for n in listA if n % 2 == 1]

import numpy as np
listA = np.arange(1.0,11.0)
cube = lambda x: x ** 3
listACubed = list(map(cube, listA))

def sqr(x):
   return x ** 2
   
items_squared = map( sqr, items_list)

xlist = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 75,100]
tens_list = list(filter(lambda x: x % 10 == 0, xlist))



### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

def difference_in_days(date_start, date_stop):    
    date_format = "%m-%d-%Y"    
    date1 = datetime.strptime(date_start, date_format)    
    date2 = datetime.strptime(date_stop, date_format)    
    days = date2 - date1    
    return days.days    

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```
def difference_in_days(date_start, date_stop):    
    date_format = "%m%d%Y"    
    date1 = datetime.strptime(date_start, date_format)    
    date2 = datetime.strptime(date_stop, date_format)   
    days = date2 - date1    
    return days.days  
    
>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

def difference_in_days(date_start, date_stop):    
    date_format = "%d-%b-%Y"    
    date1 = datetime.strptime(date_start, date_format)    
    date2 = datetime.strptime(date_stop, date_format)   
    days = date2 - date1    
    return days.days 

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Write a script as indicated (using the football data) in [q8_parsing.py](python/q8_parsing.py)





