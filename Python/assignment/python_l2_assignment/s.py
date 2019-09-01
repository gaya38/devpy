class A(object):     # deriving from 'object' declares A as a 'new-style-class'
    def foo(self,x):
        print x

class B(A):
    def dis(self,x):
        super(B,self).foo(3)   # calls 'A.foo()'

myB = B()
myB.dis(4)
