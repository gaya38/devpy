try:
    o=open("file.txt","r")
    o.write("Hi this is exception handling")
except IOError:
    print "input output error occured while performing the operations on a file"
else:
    print "Program is executed"
try:
    a=5
    lst=[]
    lst.remove(a)
except ValueError:
    print "Value error occured due to incorrect operation"
else:
    print "Program is executed"
