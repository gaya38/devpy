List1=[4,3,0,5,6,1,10,11]
List2=[7,2,4,6,3,8,5]
List3=[7,5,6,4,9,8]
List1.sort()
List2.sort()
List3.sort()
Maxlist=List1[-2:]+List2[-2:]+List3[-2:]
print "maximum list:",Maxlist
a=sum(Maxlist)/len(Maxlist)
print "Avg of maximum list:",a
Minlist=List1[:2]+List2[:2]+List3[:2]
print "minimum list:",Minlist
a=sum(Minlist)/len(Minlist)
print "Avg of maximum list:",a

