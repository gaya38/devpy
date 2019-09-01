def min_max(a):
    for j in range(len(a)-1):
        for l in range(len(a)-1):
                if (len(a[l])>len(a[l+1])):
                    temp=a[l]
                    a[l]=a[l+1]
                    a[l+1]=temp
                else:
                    continue
list1=['hyderabad','vizag','chennai','pune','bangalore']
list2=['kerala','delhi','kashmir','kochi','orrisa']
list3=['kolkata','mumbai','bihar','patna','punjab']
b=[]
print "name of the city in list and their length"
for i in list1:
    print i,':',len(i)
for i in list2:
    print i,':',len(i)
for i in list3:
    print i,':',len(i)
print "maximum and minimum elements of each list"
min_max(list1)
print list1
b.append(list1[0])
b.append(list1[-1])
print list1[-1],':',len(list1[-1])
print list1[0],':',len(list1[0])
min_max(list2)
print list2
b.append(list2[0])
b.append(list2[-1])
print list2[-1],':',len(list2[-1])
print list2[0],':',len(list2[0])
min_max(list3)
print list3
b.append(list3[0])
b.append(list3[-1])
print list3[-1],':',len(list3[-1])
print list3[0],':',len(list3[0])
print "Compare each list and determine which city is biggest & smallest with length"
print b
min_max(b)
print b[-1],':',len(b[-1])
print b[0],':',len(b[0])
print "deleting first and last element of each list and print list contents"
del(list1[0],list1[-1])
print "List1 after deleting:",list1
del(list2[0],list2[-1])
print "List2 after deleting:",list2
del(list3[0],list3[-1])
print "List3 after deleting:",list3



