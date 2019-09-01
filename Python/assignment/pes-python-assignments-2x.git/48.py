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
a=input("Enter the a value:")
b=input("Enter the b value:")
print "Addition of a and b : ", add(a,b)
print "Substraction of a and b : ", sub(a,b)
print "Multiplication of a and b : ", mul(a,b)
print "Division of a and b : ", div(a,b)
n=input("Enter the n value to find the sqrt:")
print "Square root of a given function:",sqrt(n)
string="Pack:My:Box:With:Good:Food"
print "List of the strings:",strlst(string,':')

