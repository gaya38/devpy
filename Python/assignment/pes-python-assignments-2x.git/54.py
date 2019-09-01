print "Executing the exceptions:"
try:
    a=input("Enter the a value:")
    b=input("Enter the b value:")
    c=a+b
    while (a>b):
        print "infinite loop"
except KeyboardInterrupt:
    print "Program has been stoppped forcefully because of infinite loop"
else:
    print "Sum of a and b is:",c
try:
    d=inpit("Enter the d value:")
except NameError:
    print "Built in function is wrong in the try block"
else:
    print "Program is executed"
try:
    i=input("Enter the a value:")
    j=input("Enter the b value:")
    k=i/j
except ArithmeticError:
    print "The operation is invalid"
else:
    print "division of i and j is:",k
