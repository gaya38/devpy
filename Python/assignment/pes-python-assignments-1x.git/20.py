n=input("Enter the constraint to print no of fibanocci values:")
m=input("Enter the maximum value to print the fibanocci values:")
a=0
b=1
print "Fibanocci series"
print a
print b
k=1
for i in range(1,m+1):
    if (k<(m+1)):
        print k
        a=b
        b=k
        k=a+b     
    else:
        break



        



