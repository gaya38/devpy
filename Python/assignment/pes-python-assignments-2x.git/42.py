def fib(n):
    if (n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return(fib(n-1)+fib(n-2))
    
n=input("Enter the number to print fibonacci series:")
print "fibonacci series:"
for i in range(n):
    a=fib(i)
    print a
