class Solution(object):
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        
        The critical problem is how to represent the shape of an island?
        - Area & xy bounardy is not enough
        - The shape of the island can be represented by taking the relative position of the connected cells from the leftmost cell on the top row of the island (the first cell of each island we will visit). For each island we visit, we are guaranteed to visit the top row's leftmost cell first if we iterate the matrix row by row, left to right direction. We will get the same order of cells for islands of the same shape if we perform the search in a consistent manner.
        """
        def check(i,j, land):
            if not 0<=i<m or not 0<=j<n or grid[i][j]!=1:
                return land
            grid[i][j]=2
            land.append((j-land[0][0], i-land[0][1]))
            land = check(i+1,j,land)
            land = check(i-1,j,land)
            land = check(i,j+1,land)
            land = check(i,j-1,land)
            return land
            
            
        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])
        islands = set()
        
        
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x==1:
                    land = check(i,j, [(j,i)])
                    islands.add(tuple(land[1:]))
      
        return len(islands)
