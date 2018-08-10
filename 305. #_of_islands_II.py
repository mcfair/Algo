#count the number of islands after each addLand operation

#Union Find - Stefan 240ms
class Solution(object):
    
    def numIslands2(self, m, n, positions):
        parent, rank, count = {}, {}, [0]
        def find(x):
            return x if x== parent[x] else find( parent[x])
    
        def union(x, y):
            x, y = find(x), find(y)
            if x != y:
                if rank[x] < rank[y]:
                    x, y = y, x
                parent[y] = x
                rank[x] += rank[x] == rank[y]
                count[0] -= 1
                
        def add((i, j)):
            x = (i, j)
            parent[x], rank[x]  = x, 0
            count[0] += 1
            for y in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
                if y in parent:
                    union(x, y)
            return count[0]
        
        return map(add, positions)
    
    
class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
     
        f = UnionFind(m,n)
        return map(f.add, positions)

#TLE myself TLE
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
    
