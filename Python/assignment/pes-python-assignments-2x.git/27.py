import string
n=raw_input("Enter the string to find whether it is palindrome or not:")
a=''.join(reversed(n))
if (a==n):
    print "The given string is palindrome"
else:
    print "The given string is not a palindrome"
    
