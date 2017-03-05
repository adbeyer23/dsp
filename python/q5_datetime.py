# Hint:  use Google to find python function

####a) 
date_startA = '01-02-2013'  
date_stopA = '07-28-2015'   

####b)  
date_startB = '12312013'  
date_stopB = '05282015'  

####c)  
date_startC = '15-Jan-1994'  
date_stopC = '14-Jul-2015'  

formatA = "%m-%d-%Y"
formatB = "%m%d%Y"
formatC = "%d-%b-%Y"

def find_date_diff(date_start, date_stop, format1):
    timedelta_start = datetime.datetime.strptime(date_start, format1)
    timedelta_end = datetime.datetime.strptime(date_stop, format1)
    return timedelta_end - timedelta_start
  
print(find_date_diff(date_startA, date_stopA, formatA))
print(find_date_diff(date_startB, date_stopB, formatB))
print(find_date_diff(date_startC, date_stopC, formatC))
