class Mymath:
    def sqroot(self,x):
        return (x**(0.5)) 
    def addition(self,x,y):
        return (x+y)
    def substraction(self,x,y):
        return (x-y)
    def multiplication(self,x,y):
        return (x*y)
    def division(self,x,y):
        return (x/y)
m=Mymath()
print "Square root of x:",m.sqroot(25)
print "Addition of x and y:",m.addition(2,2)
print "Substraction of x and y:",m.substraction(10,5)
print "Multiplication of x and y:",m.multiplication(10,5)
print "Division of x and y:",m.division(10,5)
