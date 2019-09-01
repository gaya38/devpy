a=[]
k=0
for i in range(5):
    c=raw_input("Enter the name:")
    a.append(c)
print "To check the presence of an element:"
b=raw_input("Enter the name to verify:")
if (b in a):
    print "True"
else:
    print "False"
print "Perform above activity with different method:"
for i in range(5):
    if (b==a[i]):
        k=k+1
    else:
        continue
if (k>0):
    print "True"
else:
    print "False"

print "print the reverse list of a"
a.reverse()
print a


