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
print "find out how much CPU time is taken for the execution"
list1=['hyderabad','vizag','chennai','pune','bangalore']
list2=['kerala','delhi','kashmir','kochi','orrisa']
list3=['kolkata','mumbai','bihar','patna','punjab']
print "name of the city in list and their length"
for i in list1:
    print i,':',len(i)
for i in list2:
    print i,':',len(i)
for i in list3:
    print i,':',len(i)
print time.clock(), "seconds process time"
print time.time() - t1, "seconds wall time"
