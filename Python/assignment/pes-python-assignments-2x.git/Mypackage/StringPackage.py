def encode():
    i=97
    while(i<124):
        print i,":",chr(i)
        i=i+1
    print "Please use number 123 to word seperation"
    n=input("Enter the encode message in number format without spaces:")
    a=str(n)
    c=" "
    i=0
    while(i<(len(a))):
          if (a[i:i+2]<str(97)):
                b=a[i:i+3]
                i=i+3
          else:
                b=a[i:i+2]
                i=i+2  
          c=c+(chr(int(b)))
    print "The decrypted message is:",c[1:]
def palindrome():
    n=raw_input("Enter the string to find whether it is palindrome or not:")
    a=''.join(reversed(n))
    if (a==n):
        print "The given string is palindrome"
    else:
        print "The given string is not a palindrome"
def vowels():
    n=raw_input("Enter the string to count the vowels present:")
    vow=['a','A','e','E','i','I','o','O','u','U']
    a=0;e=0;i=0;o=0;u=0;count=0
    for j in range(len(n)):    
        if (n[j] in vow):
            count=count+1
            if (n[j] in vow[:2]):
                a=a+1            
            elif(n[j] in vow[2:4]):
                e=e+1            
            elif(n[j] in vow[4:6]):
                i=i+1         
            elif(n[j] in vow[6:8]):
                o=o+1           
            elif(n[j] in vow[8:]):
                u=u+1            
            else:
                continue
        else:
            continue
    print "Total Vowel count:",count
    print "Vowel:a and Count:",a
    print "Vowel:e and Count:",e
    print "Vowel:i and Count:",i
    print "Vowel:o and Count:",o
    print "Vowel:u and Count:",u
def sort():
    n=input("Enter the n value for list:")
    a=[]
    for i in range(n):
        b=input("enter the b value:")
        a.append(b)
    print "The list of elements:",a
    for j in range(len(a)):
        for k in range(len(a)-1):
            if(a[k]>a[k+1]):
                temp=a[k]
                a[k]=a[k+1]
                a[k+1]=temp
            else:
                continue
    print "the sorted list:",a
def binary():
    a=[10,20,30,40,50,60]
    n=input("Enter the n value for list:")
    print "The list of elements:",a
    low=0
    high=len(a)-1
    i='not found'
    while (low<=high and i=='not found'):
        m=(low+high)/2
        if (a[m]==n):
            i='found'        
        else:
            if n<a[m]:
                high=m-1
            else:
                low=m+1
    if (i=='not found'):
        print "Unsuccessful search"
    else:
        print "Success"






