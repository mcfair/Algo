# 44ms 
# If m operations (here m edges), either Union or Find, are applied to n elements, 
# the total run time is O(m log*n), where log* is the iterated logarithm. ~=O(4m)= O(m)
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
        
#use dict to save space for sparse graph   
class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        
        self.papa = {}
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
        if a != self.papa.setdefault(a,a):
            self.papa[a] = self.find(self.papa[a])
        return self.papa[a]
