class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        
        m , n, ans = len(grid), len(grid[0]), 0
        
        
        def dfs(i,j):
            if not 0<=i<m or not 0<=j<n or grid[i][j]!='1':
                return 
            grid[i][j] ='#'
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j-1)
            dfs(i,j+1)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1':
                    dfs(i,j)
                    ans +=1
        return ans
