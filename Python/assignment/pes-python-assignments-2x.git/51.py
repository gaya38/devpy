import os
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
