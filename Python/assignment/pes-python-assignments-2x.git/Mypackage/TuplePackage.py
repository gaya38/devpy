def tupbig():
    tup1=('sun','mon','tue','wed','thu','fri','sat')
    print "tuple1:",tup1
    tup2=('jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec')
    print "concatenation of tuple2 and tuple1:",tup2+tup1
    tup1=(1,2,3,4,5)
    tup2=(4,5,2,3,1,7,8,9)
    tup3=(5,6,2)
    a=len(tup1)
    b=len(tup2)
    c=len(tup3)
    print "The biggest tuple is:"
    if (a>b and a>c):
        print "tup1"
    elif(b>c):
        print "tup2"
    else:
        print "tup3"
    del tup1
    tup2=list(tup2)
    tup2.append(10)
    print tup2
def tupcmp():
    tup1=(1,2,3,4,5)
    tup2=(4,5,2,3,1,7,8,9)
    List=[3,4,2,1,5,8]
    print "tuple1:",tup1
    print "tuple2:",tup2
    print "List:",List
    print "Comparison of two tuples:",cmp(tup1,tup2)
    print "length of the tuple1:",len(tup1)
    print "length of the tuple2:",len(tup2)
    print "maximum element of the tuple1:",max(tup1)
    print "minimum element of the tuple1:",min(tup1)
    print "maximum element of the tuple2:",max(tup2)
    print "minimum element of the tuple2:",min(tup2)
    List=tuple(List)
    print "converting the list into tuple:",List
