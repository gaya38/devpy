class Base(object):
    @classmethod
    def __init__(self):
        self.x=10
        self.y=20
    @classmethod
    def displayba(self):
        print "dis base",self.x,self.y
class Derived(Base):
    @classmethod
    def __init__(self):
        super(Derived,self).__init()
        self.a=100
        self.b=200
    @classmethod
    def displayde(self):
        print "dis Derived",self.a,self.b        
ob=Derived()
ob.displayba()
ob.displayde()
print "the object:",dir(ob)
