import math
class Circle:
    def __init__(self):
        self.r=5
    def area(self):
        return (math.pi)*(self.r**2)
    def circumference(self):
        return 2*(math.pi)*self.r
c=Circle()
print "The Area of the circle :",c.area()
print "The Circumference of the circle:",c.circumference()

        
