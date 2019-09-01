class my2(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
        print x,y
v1=my2(1,2)
v2=my2(3,2)
v3=v1+v2
print v1
print v2
print v3

