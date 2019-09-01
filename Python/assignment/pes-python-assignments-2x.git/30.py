n=input("Enter the n value for list:")
a=[]
for i in range(n):
    b=input("enter the b value:")
    a.append(b)
print "The list of elements:",a
for j in range(len(a)):
    for k in range(len(a)-1):
        if(a[k]>a[k+1]):
            temp=a[k]
            a[k]=a[k+1]
            a[k+1]=temp
        else:
            continue
print "the sorted list:",a



