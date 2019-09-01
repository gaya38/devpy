import random
class ckt:
    def __init__(self,team,size,dict1):
        self.team=team
        self.size=size
        self.dict1={}
    def cteam(self):
        print self.team
        for i in range(self.size):
            a=input("Enter the name of the teammate:")
            b=random.randrange(6,36,1)
            self.dict1[a]=b
        return self.dict1
    def cnt(self):
        s=0
        for j in self.dict1:
            s=s+self.dict1[j]
        return s
t1=ckt("Team-A",5,{})
resultA=t1.cteam()
countA=t1.cnt()
t2=ckt("Team-B",5,{})
resultB=t2.cteam()
countB=t2.cnt()
print "Team-A Score:",resultA
print "Team-A Score Sum:",countA
print "Team-B Score:",resultB
print "Team-B Score Sum:",countB
if countA>countB:
    print "Team-A won the match"
else:
    print "Team-B won the match"

            
            
            
