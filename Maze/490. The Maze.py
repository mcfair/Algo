"""
The Maze I: return True or False
The Maze II: return min steps
"""

#DFS - time & space complexity is O(mn) - 68ms
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

#BFS + minHeap  108ms
class Solution:
    def hasPath(self, maze, start, destination):

        Q = [[0]+start]
        m, n = len(maze), len(maze[0])
        dirs = ((1,0),(-1,0),(0,1),(0,-1))
        
        while Q:
            d, x, y = heapq.heappop(Q)
            if [x,y]==destination:
                return True
            maze[x][y]='v'
            for i, j in dirs:
                row, col, newd = x, y, d
                while 0<=row+i<m and 0<=col+j<n and maze[row+i][col+j]!=1:
                    row, col, newd = row+i, col+j, newd+1
                if maze[row][col]==0:
                    heapq.heappush(Q, (newd,row,col))  #take the shortest path
        return False  
  
#BFS - 360ms 
#mainbody inside while loop is exactly the same as DFS
class Solution:
    def hasPath(self, maze, start, destination):

        Q = collections.deque([start])
        n = len(maze)
        m = len(maze[0])
        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))

        while Q: 
            x, y = Q.popleft()
            maze[x][y] = 'v'

            if [x,y] == destination:
                return True

            for i, j in dirs:
                row, col = x, y
                while 0 <= row+i < n and 0 <= col+j < m and maze[row+i][col+j] != 1:
                    row += i
                    col += j
              
                if maze[row][col] == 0: #TLE without if statement
                    Q.append((row, col))

        return False

