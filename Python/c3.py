class wipro:
    res=0
    def __init__(self,x=0,y=0):
        self.a=x
        self.b=y
    def calc(self):
        self.res=self.a+self.b
    def display(self):
        print self.res
ob1=wipro(10,20)
ob2=wipro()
ob2.calc()
ob2.display()
ob1.calc()
ob1.display()
print wipro.res
