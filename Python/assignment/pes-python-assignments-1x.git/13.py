a=[]
for i in range(4):
    b=input("Enter a value:")
    a.append(b)            
a.append(6)
i=0
print "Large number among the five values is:"
if(a[i]>a[i+1] and a[i]>a[i+2] and a[i]>a[i+3] and a[i]>a[i+4]):
    c=a[i]
elif(a[i+1]>a[i+2] and a[i+1]>a[i+3] and a[i+1]>a[i+4]):
    c=a[i+1]
elif(a[i+2]>a[i+3] and a[i+2]>a[i+4]):
    c=a[i+2]
elif(a[i+3]>a[i+4]):
    c=a[i+3]
else:
    c=a[i+4]
print c


