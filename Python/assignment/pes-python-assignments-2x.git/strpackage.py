import stringop
x=[]
n=input("Enter the list length:")
for i in range(n):
    b=input("Enter the b value:")
    x.append(b)
print "The list:",x
r=stringop.sort(x)
print "The sorted list is:",r
y=input("Enter the value to search in the list:")
r=stringop.binary(x,y)
print "The result:",r
x=input("Enter the string:")
stringop.reverse(x)
    
