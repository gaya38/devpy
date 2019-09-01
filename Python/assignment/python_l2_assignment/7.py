class Strlen:
    def __init__(self,length):
        self.length=length
    def __gt__(self,other):
        return len(self.length) > len(other.length)
str1=input("Enter string1:")
str2=input("Enter string2:")
s1=Strlen(str1)
s2=Strlen(str2)
print s1>s2
