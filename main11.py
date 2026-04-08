import datetime 
import time
import calendar
from datetime import deltatime,date

# FOR IMPORT DATETIME MODULE:

# FOR CHECK the exact date
today = datetime.date.today()
print(today)

#for CHEck the exact time
today1=datetime.datetime.now().time()
print(today1)   

# FOR custom time  
t=datetime.date(2024,6,5)
t2=datetime.datetime(2024,5,6,12,34,56)
print(t)
print(t2)

#FOR FORMATTING The time in any way
formatted=datetime.datetime.now().strftime("%Y:%m:%d %H:%M:%S")
print(formatted)

#CONVERT string into date
date_str="1996-05-7 12:34:56"
date_obj=datetime.datetime.strptime(date_str,"%Y-%m-%d %H:%M:%S")
print(date_obj)

#ALSO USE THEM LIKE THIS AND SEPERATELY 
now=datetime.datetime.now()
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)


# FOR IMPORT TIME MODULE:

#FOR CHECK TIME IN MILISECONDS 
print(time.time())

#FOE CHECK THE TIME IN FORMAT OF YEAR,MONTH,DAY,HOUR,MINUTE,SECOND
print(time.ctime())

#IT IS USED TO GIVE TIME IN TUPLE FORMAT
print(time.localtime())

#IT IS USED TO STOP THE EXCUTION OF THE PROGRAM FOR A SPECIFIC TIME
time.sleep(5)
print("5 seconds have passed")


# FOR IMPORT CALENDAR MODULE:

#FOR CHECK THE   MONTH
print(calendar.month(2008,12))

#FOR CHECK THE CALENDAR OF THE YEAR
print(calendar.calendar(2034))

#FOR CHECK THAT HOW MANY DAYS THE USER LIVED IN THIS WORLD
d1=datetime.datetime(2006,6,17)
d2=datetime.datetime.now()
print("You have lived for", (d2-d1).days, "days")


