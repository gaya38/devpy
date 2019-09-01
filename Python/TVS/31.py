a=[10,20,30,40,50,60]
n=input("Enter the n value for list:")
print "The list of elements:",a
low=0
high=len(a)-1
i='not found'
while (low<=high and i=='not found'):
    m=(low+high)/2
    if (a[m]==n):
        i='found'        
    else:
        if n<a[m]:
            high=m-1
        else:
            low=m+1
if (i=='not found'):
    print "Unsuccessful search"
else:
    print "Success"



