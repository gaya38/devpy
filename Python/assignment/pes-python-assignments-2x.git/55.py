def poundtokilo(pound):
    factor=2.2046226218
    assert(pound>=0)
    kilo=factor*pound
    assert(kilo<=100)
    return kilo
a=input("Enter the person weight in pounds:")
print "Converting from pounds to kilograms:"
b=poundtokilo(a)
print "Weight in kilos:",b
