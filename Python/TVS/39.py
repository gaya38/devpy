import time, calendar
currenttime=time.asctime(time.localtime(time.time()))
print ("Current date and time is:",currenttime)
y = int(input("enter the current year : "))
m = int(input("enter the current month : "))
print(calendar.month(y, m))

