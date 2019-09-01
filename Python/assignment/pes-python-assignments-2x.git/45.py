def palindrome(n):
    i=''.join(reversed(n))
    if (i==n):
        return 1
    else:
        return 0
n=raw_input("Enter the n value:")
k=palindrome(n)
if (k==1):
    print "The given string is a palindrome"
else:
    print "The given string is not a palindrome"

