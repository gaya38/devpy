a="My name is satyanarayana"
asub='is'
print "string ends with:",a.endswith(asub,0,10)
b="this is \ttab example"
print "string expanded tab:",b.expandtabs(20)
print "index of the sub string using FIND without raise an exception:",a.find(a)
print "index of the sub string using FIND without raise an exception:",a.find(a,30)
print "index of the sub string using INDEX will raise an exc if not found:",a.index(a)
print "Returns true if the string is alpha numeric:",a.isalnum()

