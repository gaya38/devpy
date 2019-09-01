class Mymath:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def sqroot(self):
        return (self.x**(0.5)) 
    def addition(self):
        return (self.x+self.y)
    def substraction(self):
        return (self.x-self.y)
    def multiplication(self):
        return (self.x*self.y)
    def division(self):
        return (self.x/self.y)
m=Mymath(10,5)
print "Square root of x:",m.sqroot()
print "Addition of x and y:",m.addition()
print "Substraction of x and y:",m.substraction()
print "Multiplication of x and y:",m.multiplication()
print "Division of x and y:",m.division()
