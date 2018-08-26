"""
The Maze I: return True or False
The Maze II: return min steps
"""

#DFS - time & space complexity is O(mn)
class Solution:
    def hasPath(self, maze, start, destination):
        
        m, n = len(maze), len(maze[0])
        
        def dfs(x, y):
            if maze[x][y]=='v': #already visited means balls are bouncing around
                return False
            if [x,y] == destination:
                return True
            maze[x][y]='v'
            
            for i, j in ((-1, 0) , (1, 0), (0, -1), (0, 1)): #moving along each direction
                newX, newY = x, y
                while 0 <= newX + i < m and 0 <= newY + j < n and maze[newX + i][newY + j] != 1:
                    newX += i
                    newY += j
                if dfs(newX, newY):
                    return True
            return False
        
        return dfs(start[0], start[1] )

