i=97
while(i<124):
    print i,":",chr(i)
    i=i+1
print "Please use number 123 to word seperation"
n=input("Enter the encode message in number format without spaces:")
a=str(n)
c=" "
i=0
while(i<(len(a))):
    if (a[i:i+2]<str(97)):
        b=a[i:i+3]
        i=i+3
    else:
        b=a[i:i+2]
        i=i+2
    c=c+(chr(int(b)))
print "The decrypted message is:",c[1:]

