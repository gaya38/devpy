a=input("Enter the length of the list:")
list1=[]
for i in range(0,a):
    b=input("Enter the list value:")
    list1.append(b)
print "Print all operators:"
for i in range(len(list1)):
    print list1[i]
print "Perform slicing:"
y=list1[:4]
print y
print "Perform repetition:"
print y*4
print "Perform concatenation with another list:"
print list1+y



