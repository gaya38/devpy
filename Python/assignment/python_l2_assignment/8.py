import math
class Circle:
    def area(self,r):
        return (math.pi)*(r**2)
    def circumference(self,r):
        return 2*(math.pi)*r
c=Circle()
r1=input("Enter the radius:")
print "The Area of the circle is with radius ",r1,":",c.area(r1)
print "The Circumference of the circle is with radius ",r1,":",c.circumference(r1)

        
