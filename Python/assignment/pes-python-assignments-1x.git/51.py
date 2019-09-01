x=raw_input("Enter the program driver as arg or big:")
if(x=='arg'):
    a=raw_input("Enter a value:")
    e=[]
    g=0
    for i in range(len(a)):
        if (a[i]==" ")or(i==len(a)-1):
            e.append(a[g:i+1])
            g=i+1
        else:
            continue
    for i in e:
        print i
elif(x=='big'):
    b=input("Enter b value:")
    k=[]
    while(b>0):
        k.append(b%10)
        b=b/10
    for l in range(len(k)-1):
        if (k[l]>k[l+1]):
            temp=k[l]
            k[l]=k[l+1]
            k[l+1]=temp
        else:
            continue
    print k[-1]
else:
    print "Entered the wrong value so program ended"

