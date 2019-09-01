import calendar
print "printing the 2016 calendar:"
cal=calendar.calendar(2016,w=2,l=1,c=10)
print cal
yr=1980
n=0
for yr in range(1980,2025):
    i=calendar.isleap(yr)
    if i is True:
        n=n+1
    else:
        continue
print "the number of leap years between 1980 and 2025 is:",n
year=input("Enter the year:")
j=calendar.isleap(year)
if j is True:
   print "The year %d is a leap year"%year
else:
    print "The year %d is not a leap year"%year
mon=input("Enter any month number:")
k=calendar.month(2016,mon)
print "The calander of speciied month is:"
print k
    
