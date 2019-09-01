def add(x,y):
    return (x+y)
def diff(x,y):
    return (x-y)
def mul(x,y):
    return (x*y)
def div(x,y):
    return (x/y)
def sqrt(x):
    return (x**(0.5))
def floordiv(x,y):
    return (x//y)
def mod(x,y):
    return (x%y)
def prime(x):
    k=0
    b=(x/2)+1
    for i in range(1,b):
        if(x%i==0):
            k=k+1
        else:
            continue        
    if (k==1):
        return "The given number is a prime number"
    else:
        return "The given number is not a prime number"
def fib(x):
    a=0
    b=1
    print "Fibanocci series"
    print a
    print b
    k=1
    for i in range(1,x+1):
        if (k<(x+1)):
            print k
            a=b
            b=k
            k=a+b     
        else:
            break

