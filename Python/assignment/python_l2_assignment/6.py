class Matrix:
    def __init__(self,id):
        self.id=id
    def __add__(self,other):
        for i in range(2):
            for j in range(2):
                self.id[i][j]=self.id[i][j]+other.id[i][j]
        return self.id
l1=[[1,2],[3,4]]
l2=[[1,3],[2,3]]
m1=Matrix(l1)
m2=Matrix(l2)
print m1+m2


