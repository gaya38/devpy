class Int:
    t=1 # class specific
    def __init__(self,v): #v is instance specific
        self.v=v
    def __add__(self,v):
        # returns a new instance
        return Int(self.v+v)
    def __sub__(self,v):
        # returns a new instance
        return Int(self.v-v) 
    def __iadd__(self,v):
        #modify existing instance
        self.v += v
        return self
       # return Int(self.v+v)
    def prnt(self):
        print(self.v)
x=Int(5)
x.prnt()
y=x+3#invokes __add__
y.prnt()
x.prnt()
x+=3#invokes __iadd__
x.prnt()
k=x-3
k.prnt()
