f=open("op.txt",'r')
text=f.read()
print "File is in read mode:"
print text
f.close()
f=open("op.txt",'rb')
text=f.read()
print "File is in read binary mode:"
print text
f.close()
f=open("op.txt",'r+')
text=f.read()
print "File is in read and write mode:"
print text
f.close()
f=open("op.txt",'rb+')
text=f.read()
print "File is in read and write binary mode:"
print text
f=open("op.txt",'w')
f.write("New text in the file")
print "File is in write mode"
f.close()
f=open("op.txt",'r')
text=f.read()
print text
f.close()
f=open("op.txt",'wb')
f.write("New text in the file of binary mode")
print "File is in write binary mode"
f.close()
f=open("op.txt",'r')
text=f.read()
print text
f.close()
f=open("op.txt",'w+')
f.write("back to old file")
print "File is in write and read mode"
f.close()
f=open("op.txt",'wb+')
f.write("old text in the file")
print "File is in write and read binary mode"
f.close()
f=open("op.txt",'a')
f.write("appending New text in the file")
print "File is in append mode"
f.close()
f=open("op.txt",'r')
text=f.read()
print text
f.close()
f=open("op.txt",'ab')
f.write("appending binary New text in the file")
print "File is in append binary mode"
f.close()
f=open("op.txt",'r')
text=f.read()
print text
f.close()
f=open("op.txt",'a+')
f.write("appending New text in the file")
print "File is in append and read mode"
f.close()
f=open("op.txt",'ab+')
f.write("appending binary New text in the file")
print "File is in append and read binary mode"
f.close()




