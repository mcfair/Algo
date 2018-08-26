class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        dp = grid[:]  #we can also do DP inplace, without copying grid, making O(1) space
        
        #base cases: first row and first col
        for j in range(1,n):
            dp[0][j] += dp[0][j-1]
        for i in range(1,m):
            dp[i][0] += dp[i-1][0]
            
        #O(mn)
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] += min(dp[i-1][j], dp[i][j-1]) 
                
        return dp[m-1][n-1]
