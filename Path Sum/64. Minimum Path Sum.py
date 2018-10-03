#Asked in Amazon on-site 09/21
"""
This is array problem, not a tree problem.
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, 
which minimizes the sum of all numbers along its path.
"""
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

 """
 Amazon's Follow-up to backtrack the actual path.
 """
 class Solution(object):
    def minPathSum(self, grid):

        m, n = len(grid), len(grid[0])
        dp = collections.defaultdict(lambda:float('inf'))
        parent = {}
       
        for i in range(m):
            for j in range(n):   
                dp[i,j]=grid[i][j]
        
        for i in range(m):
            for j in range(n):    
                if (i,j)!=(0,0): 
                    if dp[i-1,j] < dp[i,j-1]:
                        parent[i,j] = (i-1,j)
                        dp[i,j] +=  dp[i-1,j]
                    else:
                        parent[i,j] = (i,j-1)
                        dp[i,j] +=  dp[i,j-1]
       
        path = [(m-1,n-1)]            
        while path[0]!=(0,0):
            path =[parent[path[0]]] + path
  
        return dp[m-1,n-1]
