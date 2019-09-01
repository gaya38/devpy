from string import maketrans
a="My name is gayathri123"
asub='is'
b="Is Title"
s="     thanks for removing extra space"
d="thanks for removing trailing space                "
print len(d)
print len(d.rstrip())
seq=('1','2','3')
c='*'
print "converts the string into lower letters for b:",b.lower()
print "removes leading white space for s:",s.lstrip()
intab='ai'
outtab='38'
trans=maketrans(intab,outtab)
print "encode the string using maketrans():",a.translate(trans)
print "max character:",max(a)
print "min character:",min(a)



