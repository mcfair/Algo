"""
One weired thing is that if I don't use have a seperate for loop to do initial count, the result is wrong.
Not sure why I can't setup self.papa and self.count inside "find" function.
"""
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
            
        self.papa = {}
        self.rank = {}
        self.count = 0
        m , n = len(grid), len(grid[0])  
        
        #setup parent and count++
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1':        
                    x = (i,j)
                    self.papa[x]=x
                    self.rank[x]=0
                    self.count +=1
        
        #union
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1':
                    for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                        if 0<=i+dx<m and 0<=j+dy<n and grid[i+dx][j+dy]=='1':
                            self.union((i,j), (i+dx,j+dy))
        return self.count
        
    def find(self, x):
            
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
