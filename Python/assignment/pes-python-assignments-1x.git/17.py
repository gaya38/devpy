a=[]
n=input("Enter the n value:")
for i in range(n):
    b=input("Enter a value:")
    a.append(b)            
print "Large number among the list a:"
for l in range(len(a)-1):
        if (a[l]>a[l+1]):
            temp=a[l]
            a[l]=a[l+1]
            a[l+1]=temp
        else:
            continue
print a[-1]
print "Small number among the list a:"
for l in range(len(a)-1):
        if (a[l]<a[l+1]):
            temp=a[l]
            a[l]=a[l+1]
            a[l+1]=temp
        else:
            continue
print a[-1]


