class Date:
   mths = ['JAN', 'FEB', 'MAR', 'APR']
   # note: mths is shared by all instances
   def __init__(self, dd, mm, yy):
      self.dd = dd
      self.mm = mm
      self.yy = yy
      self.sep = '/'
      self.fmt = 'ddmmyy'
   
   def setFormat(self, sep, fmt):
      self.sep = sep
      self.fmt = fmt
   def prnt(self):      
      print(str(self.dd)+self.sep \
        + str(self.mm)+self.sep \
        + str(self.yy))
   def __str__(self):
      if self.fmt == 'ddmmyy':
        return (str(self.dd)+self.sep \
          + str(self.mm)+self.sep \
          + str(self.yy))
      elif self.fmt == 'ddmmmyy':
        return (str(self.dd)+self.sep \
          + Date.mths[self.mm-1]+self.sep \
          + str(self.yy))
      else:
        print('invalid format specifier')
  
d1 = Date(8,3,2018)
d2 = Date(10,1,2018)
d1.setFormat('/', "ddmmyy")
d1.prnt()  # uses print() defined in the class
d2.setFormat('-', "ddmmmyy")
print(d2)   # uses __
