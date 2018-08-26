"""
Union Find
Idea: 
go through the grid by the order of its value grid[i][j] 
increment time and union its reachable neighbours (grid[i][j] < t)
"""
class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid)  , len(grid[0])
        self.papa = { }
        self.rank = collections.defaultdict(int)
        
        pos = {}
        for i in range(m):
            for j in range(n):
                pos[grid[i][j]] = (i,j)
        
        for t in range(m*n): #count the clock, access 
            i,j = pos[t]
            for x, y in ((i+1,j),(i-1,j),(i,j-1),(i,j+1)): #union its reachable neighbours
                if 0<=x<m and 0<=y<n:
                    if grid[x][y]< t: 
                        self.union((i,j),(x,y))
                        if self.find((0,0))==self.find((m-1,n-1)):
                            return t
        return -1
        
    def find(self, x): #find with path compression
        if x not in self.papa:
            self.papa[x] = x
        while self.papa[x] !=x:
            x, self.papa[x] = self.papa[x], self.papa[self.papa[x]]
        return x
    
    def union(self, x,y): #union by rank  - "without rank, it will be TLE"
        x, y = self.find(x), self.find(y)
        if x!=y:
            if self.rank[x] > self.rank[y]:
                self.papa[y] = x
            elif self.rank[x] < self.rank[y]:
                self.papa[x] = y
            else:
                self.papa[y] = x
                self.rank[x] +=1
