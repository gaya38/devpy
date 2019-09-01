def search(i):
    if (a[i]==n):
        return 1
    else:
        return 0
n=input("Enter the n value for list:")
b=0
i=0
a=[10,20,30,40,50,60]
while(i<len(a) and b==0):
    b=search(i)
    i=i+1
if (b==1):
    print "Successful search"
else:
    print "Unsuccessful search"

