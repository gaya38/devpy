import sys
x=len(sys.argv)
a=[]
i=1
while(i<x):
    a.append(sys.argv[i])
    i=i+1
print "The list of command line arguments:"
print a
for l in range(len(a)-1):
        if (a[l]>a[l+1]):
            temp=a[l]
            a[l]=a[l+1]
            a[l+1]=temp
        else:
            continue
print "The large value among them:"
print a[-1]
