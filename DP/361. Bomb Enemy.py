#O(n^2)
class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])
        
        L=collections.defaultdict(int)
        R=collections.defaultdict(int)
        U=collections.defaultdict(int)
        D=collections.defaultdict(int)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]!='W':
                    L[i,j] = L[i,j-1] + (grid[i][j]=='E')
            for j in range(n-1, -1, -1):
                if grid[i][j]!='W':
                    R[i,j] = R[i,j+1] + (grid[i][j]=='E')
                    
        for j in range(n):
            for i in range(m):
                if grid[i][j]!='W':
                    D[i,j] = D[i-1,j] + (grid[i][j]=='E')
            for i in range(m-1, -1, -1):
                if grid[i][j]!='W':
                    U[i,j] = U[i+1,j] + (grid[i][j]=='E')
        
        maxkill = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='0':
                    maxkill = max(maxkill,  L[i,j]+R[i,j]+U[i,j]+D[i,j] )
        return maxkill
        
 #O(n^3)
 class Solution(object):
    def maxKilledEnemies(self, grid):
      
        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])
        
        def check(x,y):
            enemies = 0
            i, j = x, y
            while i>0 and grid[i][j]!='W':
                i-=1
                enemies += grid[i][j]=='E'
            i, j = x, y
            while i<m-1 and grid[i][j]!='W':
                i+=1
                enemies += grid[i][j]=='E'
            i, j = x, y    
            while j>0 and grid[i][j]!='W':
                j-=1
                enemies += grid[i][j]=='E'
            i, j = x, y
            while j<n-1 and grid[i][j]!='W':
                j+=1
                enemies += grid[i][j]=='E'
            return enemies        
        
        maxkill = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='0':
                    maxkill = max(maxkill,  check(i,j) )
        return maxkill

        
  
