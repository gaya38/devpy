class Sqroot(object):
    def sqrt(self,x):
        return (x**(0.5))
class Addition(object):
    def add(self,x,y):
        return (x+y)
class Substraction(object):
    def sub(self,x,y):
        return (x-y)
class Multiplication(object):
    def mul(self,x,y):
        return (x*y)
class Division(object):
    def div(self,x,y):
        return (x/y)
class Mymath(Sqroot,Addition,Substraction,Multiplication,Division):
    def display(self):
        print "Square root of x:",super(Mymath,self).sqrt(25)
        print "Addition of x and y:",super(Mymath,self).add(2,2)
        print "Substraction of x and y:",super(Mymath,self).sub(10,5)
        print "Multiplication of x and y:",super(Mymath,self).mul(10,5)
        print "Division of x and y:",super(Mymath,self).div(10,5)
c=Mymath()
c.display()
