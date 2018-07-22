class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        self.papa = [i for i in range(n)]
        self.count = n
        for a, b in edges:
            self.union(a,b)
            
        return self.count
    
    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a!=b:
            self.papa[a] = b
            self.count -=1
    
    def find(self, a):
        if a != self.papa[a]:
            self.papa[a] = self.find(self.papa[a])
        return self.papa[a]
        
    
