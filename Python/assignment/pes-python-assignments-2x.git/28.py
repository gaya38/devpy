import string
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

    
