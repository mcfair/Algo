class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        uf = UnionFind()
        ret = []
        for p in map(tuple, positions):
            uf.add(p)
            ret.append(uf.count)
        return ret

#TLE
class UnionFind(object):
    def __init__(self):
        self.parent = {}
        self.count = 0
        
    def add(self, x):
        self.parent[x] = x
        self.count +=1
        for dx,dy in [(-1,0),(1,0),(0,1),(0,-1)]:
            neighbour = (x[0]+dx, x[1]+dy)
            if self.find(neighbour):
                self.union(neighbour, x)
        
     
    def find(self,x):
        if x not in self.parent:
            return None
        
        while x is not self.parent[x]:
            #with path compression
            x, self.parent[x] = self.parent[x], self.parent[self.parent[x]]
        return x
    
    def union(self, a,b):
        pa, pb = self.find(a), self.find(b)
        if pa and pb and pa!=pb:   
            self.parent[pa] = pb
            self.count -=1        
    
