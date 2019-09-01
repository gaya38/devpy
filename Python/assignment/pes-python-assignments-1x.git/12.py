list1=[]
list2=[]
list3=[]
for i in range(0,10):
    b=input("Enter the list value:")
    list1.append(b)
print "Print the avg of all the numbers:"
c=0
for i in range(len(list1)):
    c=c+list1[i]
c=c/len(list1)
print c
print "Print all the numbers which are less than the avg:"
for i in range(len(list1)):
    if(c>list1[i]):
        print list1[i]
    elif(c<list1[i]):
        list2.append(list1[i])
    else:
        list3.append(list1[i])
print "Print all the numbers which are greater than the avg:"
print list2
print "Print all the numbers which are equals to the avg:"
print list3




