def sort(a):
    for j in range(len(a)):
        for k in range(len(a)-1):
            if(a[k]>a[k+1]):
                temp=a[k]
                a[k]=a[k+1]
                a[k+1]=temp
            else:
                continue
    return a
def binary(a,n):
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
        r="Unsuccessful search"
    else:
        r="Success"
    return r
def reverse(a):
    a=''.join(reversed(a))
    print "The reverse string is:",a











