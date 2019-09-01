import sys
print "Executing the exceptions:"
try:
    raise StandardError
except StandardError:
    print "StandardError occured"
else:
    print "Program executed"
try:
    a=input("Enter the a value:")
    b=input("Enter the b value:")
    c=a+b
    while (a>b):
        print "infinite loop"
except KeyboardInterrupt:
    print "KeyboardInterrupt occured and Program has been stoppped forcefully because of infinite loop"
else:
    print "Sum of a and b is:",c
try:
    d=inpit("Enter the d value:")
except NameError:
    print "Built in function is wrong in the try block"
else:
    print "Program is executed"
try:
    i=input("Enter the i value:")
    j=input("Enter the j value:")
    k=i/j
except ArithmeticError:
    print "ArithmeticError occurs due to invalid operation"
else:
    print "division of i and j is:",k
try:
    i=input("Enter the i value:")
    j=input("Enter the j value:")
    k=i/j
except ZeroDivisionError:
    print "ZeroDivisionError occurs due to invalid operation"
else:
    print "division of i and j is:",k
try:
    o=open("file.txt","r")
    o.write("Hi this is exception handling")
except IOError:
    print "input output error occured while performing the operations on a file"
else:
    print "Program is executed"
try:
    a=5
    lst=[]
    lst.remove(a)
except ValueError:
    print "Valueerror occurs due to incorrect operation"
else:
    print "Program is executed"
i=1
try:
    f = 3.0**i
    for i in range(100):
        f = f ** 2
except OverflowError:
    print "OverflowError occurs because of the program"
else:
    print "Program executed"
try:
    a=input("Enter the person weight in pounds:")
    assert(a>=0)
except AssertionError:
    print "AssertionError occurs due to negative input value"
else:
    print "Value of a is:",a
try:
    a=input("Enter the a value:")
    b=input("Enter the b value:")
    c=a/b
    print c
except TypeError:
    print "TypeError occurs due to unsupported operation"
else:
    print "Value of c is:",c
try:
    x=100
    y=input("Enter the y value:")
    x=float(x)
    y=float(y)
    if y==0:
        raise FloatingPointError
    else:
        x=x/y
except FloatingPointError:
    print "FloatingPointError occurs due to zero division of float values"
else:
    print "program executed and value of x is:",x
try:
    import matrix
    a=matrix.sqrt(9)
    print a
except ImportError:
    print "ImportError occurs"
else:
    print "Program executed"
try:
    import math
    a=math.int(9.0)
    print a
except AttributeError:
    print "AttributeError occurs"
else:
    print "Program executed"
try:
    a=open("file.txt","r")
    b=a.read()
    k=input("enter k value:")
    j=len(b)-k
    for i in range(j+1):
        if i==len(b):
            raise EOFError
        else:
            continue
except EOFError:
    print "EOFError raised"
else:
    print "program executed"
try:
    a=[2,3,1]
    i=input("Enter the index value:")
    print a[i]
except LookupError:
    print "LookupError raised"
else:
    print "program executed"
try:
    a=[2,3,1]
    i=input("Enter the index value:")
    print a[i]
except IndexError:
    print "IndexError raised"
else:
    print "program executed"
try:
    d={"n01":2,"n02":3,"n03":1}
    i=input("Enter the index value:")
    print d[i]
except KeyError:
    print "KeyError raised"
else:
    print "program executed"
try:
    counter = 0
    def increment():
      counter += 1
    increment()
except UnboundLocalError:
    print "UnboundLocalError occurs"
else:
    print "program executed"
try:
    a=open("abcd.txt","r")
except EnvironmentError:
    print "EnvironmentError occurs"
else:
    print "program executed"
try:
     a=input("Enter the input:")
     if (a>1):
         sys.exit()
except SystemExit:
    print "SystemExit occurs"
else:
    print "program executed"
try:
    raise SyntaxError
except SyntaxError:
    print "SyntaxError occurs"
else:
    print "program executed";    
try:
    raise IndentationError
except IndentationError:
    print "IndentationError occurs"
else:
    print "program executed"
try:
    raise SystemError
except SystemError:
    print "SystemError occurs"
else:
    print "program executed"
try:
   class Super(object):
        @property
        def example(self):
            raise NotImplementedError("Subclasses should implement this!")
   s = Super()
   print s.example
except NotImplementedError:
    print "NotImplementedError occurs"

