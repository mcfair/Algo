class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        self.parent = {}
        
        for u, v in edges:
            if self.find(u)!=self.find(v):
                self.union(u,v)
            else:
                return [u,v]
        return
    
    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
        return x if x==self.parent[x] else self.find(self.parent[x])
    
    def union(self, a,b):
        pa, pb = self.find(a), self.find(b)
        self.parent[pb] = pa
