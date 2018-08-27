
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
     
        if not M or not M[0]:
            return 0
        
        m = len(M) 
        self.papa = {}
        self.rank = {}
        self.count= 0
        for i in range(m):
            for j in range(i,m):
                if M[i][j]==1:
                    self.union(i,j)
        return self.count
        
    def find(self, x):
        if x not in self.papa:
            self.papa[x]=x
            self.rank[x]=0
            self.count +=1
            
        while x!=self.papa[x]:
            x, self.papa[x] = self.papa[x], self.papa[self.papa[x]]
            
        return x
    
    def union(self,x,y):
        x, y = self.find(x), self.find(y)
        if x!=y:
            if self.rank[x] < self.rank[y]:
                self.papa[x] = y
            elif self.rank[x] > self.rank[y]:
                self.papa[y] = x
            else:
                self.papa[y] = x
                self.rank[x] +=1
            self.count -=1
