
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
     
        if not M or not M[0]:
            return 0
        m = len(M)
        
        self.parent = {}
        self.count = 0
        
        for i in range(m):
            for j in range(i,m):
                if M[i][j]==1:
                    self.union(i,j)

        return self.count
         
    
    def find(self,x):
        if x not in self.parent:
            self.parent[x] = x     
            self.count+=1
        #return x if x==self.parent[x] else self.find(self.parent[x])
        while x!= self.parent[x]:
            x, self.parent[x] = self.parent[x], self.parent[self.parent[x]]
        return x
        
    def union(self,a,b):
        pa, pb = self.find(a), self.find(b)
        if pa!=pb:
            self.parent[pb] = pa
            self.count-=1
          
