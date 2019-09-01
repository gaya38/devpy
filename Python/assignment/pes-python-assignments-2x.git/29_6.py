a="My name is gayathri123 and this is a program"
asub='is'
print "replace the string with a new charcter:",a.replace("is","was",2)
print "finds a string with rfind:",a.rfind(asub,0,30)
print "finds a string with rindex:",a.rindex(asub,0,30)
print "string padding from left:",a.rjust(50,'%')
c=a.ljust(50,'*')
print c
print "removes extra space in c:",c.rstrip('*')



