import time
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
