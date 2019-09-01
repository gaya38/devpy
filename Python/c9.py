class First(object):
    @classmethod
    def __init__(self):
        self.x1=1
        self.y1=2
    def display(self):
        print "first display"
class Second(First):
    @classmethod
    def __init__(self):
        #super(Second,self).__init__()
        self.x2=10
        self.y2=20
    def display(self):
        super(Second,self).display()
        print "Second display"
class Third(Second):
    @classmethod
    def __init__(self):
        super(Second,self).__init__()
        self.x3=100
        self.y3=200
ob=Third()
print "ob first:",ob.x1,ob.y1
print "ob first:",ob.x3,ob.y3
ob.display()
