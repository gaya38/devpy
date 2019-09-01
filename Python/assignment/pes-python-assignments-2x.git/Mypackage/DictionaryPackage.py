import time
import calendar
def dictsam():
    dict1= {'Name': 'Gayathri', 'Age': 23, 'Class': 'Third'}
    dict2= {'Name': 'Geetha', 'Age': 24, 'Class': 'First'}
    dict3= {'Name': 'Mouni', 'Age': 24, 'Class': 'Second'}
    a=cmp(dict1,dict2)
    b=cmp(dict1,dict3)
    c=cmp(dict2,dict3)
    if(a==1 and b==1):
        print "dict1 is the biggest dictionary"
    else:
        if(c==1):
            print "dict2 is the biggest dictionary"
        else:
            print "dict3 is the biggest dictionary"
    dict1['Section']='A'
    dict2['Section']='B'
    print "the length of dict1 is:",len(dict1)
    print "the length of dict1 is:",len(dict2)
    print "the length of dict1 is:",len(dict3)
    dict1=str(dict1)
    dict2=str(dict2)
    dict3=str(dict3)
    print "concatenation of three strings:",dict1+dict2+dict3
def dictcpy():
    dict1 ={'Name':'Ramakrishna','Age':25}
    dict2={'EmpId':1234,'Salary':5000}
    dict3=dict1.copy()
    dict3.update(dict2)       
    print "Merging of two dictionaries:",dict3
    a=dict3['Salary']/10
    dict3['Salary']=dict3['Salary']+a
    print "After updating the salary by 10%:",dict3
    dict3['Age']=26
    print "After updating the age to 26:",dict3
    dict3['grade']='B1'
    print "After updating the dictionary with a new key grade:",dict3
    print "All values of dict:",dict.values(dict3)
    print "All keys of dict:",dict.keys(dict3)
    del dict3['Age']
    print "After the delete the Age key in dict3:",dict3
def time1():
    currenttime=time.asctime(time.localtime(time.time()))
    print "Current date and time is:",currenttime
    monthcal = calendar.month(2018, 8)
    print "Current month calendar:",monthcal
def time2():
    print "printing the current time till one minute:"
    i=0
    while(i<=12):
        currenttime=time.asctime(time.localtime(time.time()))
        print "Current date and time is:",currenttime
        time.sleep(5)
        i=i+1
    print "Calculate the process time of below program:"
    t0 = time.clock()
    t1 = time.time()
    list1=[10,20,30,40,50,60]
    list2=[10,20,30,40]
    list3=[50,60,70,80,90]
    a=len(list1)
    b=len(list2)
    c=len(list3)
    print "length of list1 is:",a
    print "length of list2 is:",b
    print "length of list3 is:",c
    print time.clock(), "seconds process time"
    print time.time() - t1, "seconds wall time"
def cal1():
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

    


    
