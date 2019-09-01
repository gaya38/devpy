f=open("file.txt","r")
text=f.readlines()
j=0-len(text)-1
for line in range(-1,j,-1):
    print text[line]
f.close()
f1=open("file.txt","r")
text1=f1.read()
k=0-len(text1)-1
for letr in range(-1,k,-1):
    print text1[letr]
