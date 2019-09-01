class Base:
    def calc(self):
        print "calc base"
    def display(self):
        print "dis base"
class Derived(Base):
    def calc(self):
        print "calc Derived"
    def display(self):
        print "dis Derived"
        
ob=Derived()
ob.calc()
ob.display()
