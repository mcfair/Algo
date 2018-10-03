#Asked in Amazon on-site  
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
 This is what I wrote in interview.
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
"""
BFS + Heap version of backtrack, slower 
In the original problem, the rule is that we can only move down or right.
This BFS+Heap method potentially can handle complex move rules (for example, go diagonally, or even any direction).
"""
class Solution(object):
    def minPathSum(self, grid):

        m, n = len(grid), len(grid[0])
        visited = set([])
        start = grid[0][0]
        q = [(start, 0, 0, [start])]
         
        while q:
            cur_path_cost, x,y, path = heapq.heappop(q) 
            # Cell already visited with lower path_cost
            if (x,y) in visited:
                continue
            else:
                visited.add((x,y))

            # Found target
            if x==m-1 and y==n-1:
                return cur_path_cost
                
            # Go down only if there is still room to go down
            if x+1 < m:
                heapq.heappush(q, (cur_path_cost + grid[x+1][y], x+1, y, path+[grid[x+1][y]]))
                
            # Go right
            if y+1 < n:
                heapq.heappush(q, (cur_path_cost + grid[x][y+1], x, y+1, path+[grid[x][y+1]]))
                
        return -1
