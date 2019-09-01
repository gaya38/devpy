a="My name is satyanarayana"
asub='is'
print "string capitalization:",a.capitalize()
print "string padding by *:",a.center(38,'*')
print "sub string asub count:",a.count(asub,0,len(a))
a=a.encode('base64','strict')
print "encoded string:",a
a=a.decode('base64','strict')
print "decoded string:",a
