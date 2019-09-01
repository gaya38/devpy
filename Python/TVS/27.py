import string
a=raw_input("Enter the string to check whether it is palindrome or not:")
b=''.join(reversed(a))
if (a==b):
    print "The given string is palindrome"
else:
    print "The given string is not a palindrome"
    
