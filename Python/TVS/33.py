list1=['hyderabad','vizag','chennai','pune','bangalore']
list1.append('kerala')
list1.insert(4,'delhi')
print list1
list1.sort()
print "Sorted list1:",list1
list1.reverse()
print "Sorted list1 in descending order:",list1
a=len(list1)
list1.pop(a-1)
list1.pop(a-2)
list1.pop(a-3)
print "After remove the elements:",list1
