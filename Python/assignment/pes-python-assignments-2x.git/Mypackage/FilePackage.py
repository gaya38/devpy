import os
def filesam():
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
def filecnt():
    word= "Treasure"
    count=0
    for filename in os.listdir(os.getcwd()):
        f=open(filename,'r')
        text=f.read()
        if word in text:
            wrdcnt=0
            for wrd in text.split():
                if (wrd==word):
                    wrdcnt=wrdcnt+1
                else:
                    continue
            print "%s having the mentioned word"%filename
            print "Count of the %s is:"%word,wrdcnt
            count=count+1
        else:
            continue
    print "The Treasure word is present in %d files"%count
def filerd():
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

    


