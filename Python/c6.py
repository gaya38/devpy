class Base(object):
    def calc(self):
        print "calc base"
    def display(self):
        print "dis base"
class Child(Base):
    def calc(self):
        super(Child,self).calc()
        print "calc child"
    def display(self):
        super(Child,self).display()
        print "dis child"
class Derived(Child):
    def calc(self):
        super(Derived,self).calc()
        print "calc Derived"
    def display(self):
        super(Derived,self).display()
        print "dis Derived"
        
ob=Derived()
ob.calc()
ob.display()
