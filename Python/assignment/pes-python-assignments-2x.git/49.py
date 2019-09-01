f1=open("file.txt","r")
text=f1.read()
print "Content of the file is:"
print text
f1.close()
f2=open("file.txt","w")
f2.write("Writing new line-1\nNew line-2\nNew line-3\nNew line-4\nNew line-5\n")
f2.close()
f3=open("file.txt","a")
f3.write("new line-6\nNew line-7\nNew line-8\nNew line-9\nNew line-10")
f3.close()
