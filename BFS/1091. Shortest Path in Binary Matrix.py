"""
Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

    All the visited cells of the path are 0.
    All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).

The length of a clear path is the number of visited cells of this path.
"""
class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return -1
        if  grid[0][0]!=0 or grid[-1][-1]:
            return -1
        
       
        m, n = len(grid), len(grid[0])
        q = [(1,0,0)]
        heapq.heapify(q)
        
       
        while len(q) > 0:
            d,i,j = heapq.heappop(q)
            if i==m-1 and j==n-1: 
                return d
            directions = ([i+1,j],[i+1,j+1], [i,j+1], [i+1,j-1],
                      [i-1,j],[i-1,j-1],[i,j-1],[i-1,j+1])
             
            for x,y in directions:
                if 0<=x<m and 0<=y<n and grid[x][y]==0:
                    grid[x][y]=1 #visited
                    heapq.heappush(q,[d+1,x,y])
                   
                    
    
        return -1 
            
        
