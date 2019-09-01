dict1= {'Name': 'Satya', 'Age': 25, 'Class': 'Third'}
dict2= {'Name': 'Siva', 'Age': 24, 'Class': 'First'}
dict3= {'Name': 'Ayyappa', 'Age': 24, 'Class': 'Second'}
a=cmp(dict1,dict2)
b=cmp(dict1,dict3)
c=cmp(dict2,dict3)
if(a==1 and b==1):
    print "dict1 is the biggest dictionary"
else:
    if(c==1):
        print "dict2 is the biggest dictionary"
    else:
        print "dict3 is the biggest dictionary"
dict1['Section']='A'
dict2['Section']='B'
print "the length of dict1 is:",len(dict1)
print "the length of dict1 is:",len(dict2)
print "the length of dict1 is:",len(dict3)
dict1=str(dict1)
dict2=str(dict2)
dict3=str(dict3)
print "concatenation of three strings:",dict1+dict2+dict3
