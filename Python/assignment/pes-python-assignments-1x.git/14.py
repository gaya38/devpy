a=[]
b=[]
x=[]
y=input("enter input range for list a:")
z=input("enter input range for list b:")
for i in range(y):
    c=raw_input("Enter the employee id:")
    a.append(c)
for i in range(z):
    d=raw_input("Enter the employee name:")
    b.append(d) 
print "All employee names:"
for i in range(z):
    print b[i]
e=input("Enter the index:")
print "Employee id and Employee name:"
print a[e]
print b[e]
print "The employee names from 4th position to 9th position:"
print b[4:9]
print "The employee names from 3rd position:"
print b[3:]
print "Repeated list:"
f=input("Enter the number to repeat the list:")
print a*f
print b*f
print "Concatenated lists:"
print a+b
print "list a and list b elements side by side:"
if (y<z):
    m=y
else:
    m=z
for l in range(m):
    x.append(a[l])
    x.append(b[l]) 
if (y>z):
    x=x+a[(l+1):]
else:
    x=x+b[(l+1):]

print x


