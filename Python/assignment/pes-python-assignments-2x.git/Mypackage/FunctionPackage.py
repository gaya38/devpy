def fib(n):
    if (n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return(fib(n-1)+fib(n-2))
def search(a,n):
    i=0
    b=0
    for i in range(len(a)):
        if (a[i]==n):
            b=b+1
        else:
            continue
    if (b>0):
        print "Successful search"
    else:
        print "Unsuccessful search"
sum = lambda a,b: a+b
sub = lambda a,b: a-b
mul = lambda a,b: a*b
div = lambda a,b: a/b
def palindrome(n):
    i=''.join(reversed(n))
    if (i==n):
        print "The given string is a palindrome"
    else:
        print "The given string is not a palindrome"
def big(a=0,b=0,c=0,d=0):
    if (a>b and a>c and a>d):
        print "a is the large number:%d"%a
    elif(b>c and b>d):
        print "b is the large number:%d"%b
    elif(c>d):
        print "c is the large number:%d"%c
    else:
        print "d is the large number:%d"%d
def ext(tup,lst):
    lst=tuple(lst)
    tupl=tup+lst
    print tupl
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def sqrt(n):
    return (n**0.5)
def strlst(x,y):
    return x.split(y)


