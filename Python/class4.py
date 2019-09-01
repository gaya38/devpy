outer=100        # global		
class Dummy:		
   inner=200     # class member		
   def fn	self, k):	
      self.x = k		
  		
   def prnt	self):	
      print	'x = ', self.x)	
      print	'inner = ', self.inner)	
      print	'outer = ', outer)	
   @staticmethod 		
   def get_inner	):	
     return Dummy.inner		
   @staticmethod 		
   def set_inner	v):	
     Dummy.inner = v		
   		
   		
d1 = Dummy	)	
d1.fn	5)	
d1.prnt	) 	
print	'-'*10)	
d2 = Dummy	)	
d2.fn	50)	
d2.prnt	) 	
print	'-'*10)	
outer=20000		
inner=5000 # introduces in global scope		
Dummy.set_inner	15000) #  inner of Dummy changed	
d1.prnt	)	
print	'-'*10)	
d2.prnt	)	
print	'-'*10)	
print	Dummy.get_inner	))
