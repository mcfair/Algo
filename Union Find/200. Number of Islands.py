class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        
        self.papa = {}
        self.count = 0
        m , n = len(grid), len(grid[0]) 
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1':
                    self.papa[i,j] = (i,j)
                    self.count+=1

        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1':
                    for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                        if 0<=i+dx<m and 0<=j+dy<n and grid[i+dx][j+dy]=='1':
                            self.union((i,j), (i+dx,j+dy))
        return self.count
        
    def find(self,x):
        return x if x==self.papa[x] else self.find(self.papa[x])
    
    def union(self, a, b):
        pa, pb = map(self.find, (a,b))
        if pa!=pb:
            self.papa[pb] = pa
            self.count -=1
