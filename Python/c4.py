class wipro:
    res=0
    def __init__(self,x=0,y=0):
        self.a=x
        self.b=y
    def calc(self):
        wipro.res=self.a+self.b
    def display(self):
        print wipro.res
ob1=wipro(10,20)
ob2=wipro(y=4,x=3)
ob2=wipro(y=5)
ob1.calc()
ob1.display()
ob2.calc()
ob2.display()
ob3.calc()
ob3.display()
print wipro.res
