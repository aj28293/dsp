# Hint:  use Google to find python function

####a) 

from datetime import datetime

date_start = '01-02-2013'  
date_stop = '07-28-2015'   

def difference_in_days(date_start, date_stop):    
    date_format = "%m%d%Y"    
    date1 = datetime.strptime(date_start, date_format)    
    date2 = datetime.strptime(date_stop, date_format)   
    days = date2 - date1    
    return days.days


date_start = '12312013'  
date_stop = '05282015'  

def difference_in_days(date_start, date_stop):
    date_format = "%m%d%Y"
    date1 = datetime.strptime(date_start, date_format)
    date2 = datetime.strptime(date_stop, date_format)
    days = date2 - date1
    return days.days

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  

def difference_in_days(date_start, date_stop):
	date_format = "%d-%b-%Y"
	date1 = datetime.strptime(date_start, date_format)
	date2 = datetime.strptime(date_stop, date_format)
	days = date2 - date1
	return days.days

