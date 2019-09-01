class wipro:
    def __init__(self,x=0,y=0):
        self.a=x
        self.b=y
        self.res=0
        print "exec constructor"
    def calc(self):
        self.res=self.a+self.b
ob1=wipro(10,20)
ob2=wipro(30,40)
ob3=wipro()
ob1.calc()
ob2.calc()
ob3.calc()
x=ob1.res
y=ob2.res
print x,y
print ob1.a,ob1.b,ob1.res
print ob2.a,ob2.b,ob2.res
print ob3.a,ob3.b,ob3.res
