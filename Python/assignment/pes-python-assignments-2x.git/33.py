List=[10,20,30,40,50,60,70]
List.append(80)
List.insert(4,100)
print List
List.sort()
print "Sorted list:",List
List.reverse()
print "Sorted list in descending order:",List
a=len(List)
List.pop(a-1)
List.pop(a-2)
List.pop(a-3)
print "After remove the elements:",List
