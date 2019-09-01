def big(a=0,b=0,c=0,d=0):
    if (a>b and a>c and a>d):
        print "a is the large number:%d"%a
    elif(b>c and b>d):
        print "b is the large number:%d"%b
    elif(c>d):
        print "c is the large number:%d"%c
    else:
        print "d is the large number:%d"%d
        
print "Passing all the values:"
big(a=5,b=3,c=6,d=2)
print "Passing c and d only:"
big(c=6,d=2)
print "Passing a and b only:"
big(a=5,b=3)
print "Passing a,b and d only:"
big(a=5,b=3,d=2)
