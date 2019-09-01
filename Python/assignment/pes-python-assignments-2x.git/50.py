f1=open("file1.txt","r")
pos=0
text=f1.read(10)
while text:
    print text
    pos=f1.tell()
    text=f1.read(10)    
    print "Current position:",pos
f1.close()
f2=open("file1.txt","r")
text1=f2.read(100)
pos1=f2.tell()
print "100 characters of the file:"
print text1
print "Reset the position and the position number is:"
pos1=f2.seek(0,0)
print pos1
f3=open("program.txt","r")
count=0
for line in open('program.txt'):
    count = count+1
    if (count>=5):
        print line
    else:
        continue
    
    


