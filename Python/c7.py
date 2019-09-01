class Base(object):
    @classmethod
    def calc(self):
        print "calc base"
    @classmethod
    def display(self):
        print "dis base"
class Derived(Base):
    @classmethod
    def calc(self):
        super(Derived,self).calc()
        print "calc Derived"
    @classmethod
    def display(self):
        super(Derived,self).display()
        print "dis Derived"
        
ob=Derived()
ob.calc()
ob.display()

