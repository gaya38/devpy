a=[]
for i in range(4):
    b=input("Enter a value:")
    a.append(b)            
a.append(6)
print "Large number among the five values is:"
for l in range(len(a)-1):
        if (a[l]>a[l+1]):
            temp=a[l]
            a[l]=a[l+1]
            a[l+1]=temp
        else:
            continue
    
print a[-1]


