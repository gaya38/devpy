a=input("Enter a value:")
k=0
b=(a/2)+1
for i in range(1,b):
        if(a%i==0):
            k=k+1
        else:
            continue        
if (k==1):
    print "The given number is a prime number"
else:
    print "The given number is not a prime number"

print "List of prime numbers until",a,":"
for i in range(1,a+1):
    l=0
    for j in range(1,i+1):
        if(i%j==0):
            l=l+1
        else:
            continue
    if (l==2):
        print i
    else:
        continue
    
