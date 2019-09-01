n=100
a=[10,20,30,40,50]
b=[60,70,80,90]
print "the list of even numbers from 1 to 100 using for loop:"
for i in range(1,n+1):
    if (i==50):
        break
    elif(i in a):
        continue
    elif(i%2==0):
        print i
    else:
        continue
print "the list of even numbers from 1 to 100 using while loop:"
j=1
while(j<(n+1)):
      if (j==90):
        break
      elif(j in b):
        pass
      elif(j%2==0):
        print j
      else:
        pass
      j=j+1
print j





        



