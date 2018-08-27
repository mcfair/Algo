class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        if not edges: return n
        
        self.papa = {}
        self.rank = {}
        self.count =n
        
        for a, b in edges:
            self.union(a,b)
            
        return self.count
     
    def find(self, x):
        if x not in self.papa:
            self.papa[x]=x
            self.rank[x]=0
            
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
