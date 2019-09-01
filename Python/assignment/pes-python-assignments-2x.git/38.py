dict1 ={'Name':'Ramakrishna','Age':25}
dict2={'EmpId':1234,'Salary':5000}
dict3=dict1.copy()
dict3.update(dict2)       
print "Merging of two dictionaries:",dict3
a=dict3['Salary']/10
dict3['Salary']=dict3['Salary']+a
print "After updating the salary by 10%:",dict3
dict3['Age']=26
print "After updating the age to 26:",dict3
dict3['grade']='B1'
print "After updating the dictionary with a new key grade:",dict3
print "All values of dict:",dict.values(dict3)
print "All keys of dict:",dict.keys(dict3)
del dict3['Age']
print "After the delete the Age key in dict3:",dict3
