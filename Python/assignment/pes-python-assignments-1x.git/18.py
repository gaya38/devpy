n=input("Enter the n value:")
k=1
mystring="Hello World"
print "the list using for loop:"
for i in range(1,(n*2)+1):
    if (i<(n+1)):
        print k
        k=k+1
    else:
        k=k-1
        print k
l=1
j=1
print "the list using while loop:"
while(j<(n*2)+1):
    if (j<(n+1)):
        print l
        l=l+1
    else:
        l=l-1
        print l
    j+=1
print "print the string:"
for m in mystring:
    print m



        



