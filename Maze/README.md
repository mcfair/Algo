Maze I & II
```
class Solution(object):
    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        Q = [[0]+start]
        m, n = len(maze), len(maze[0])
        dirs = ((1,0),(-1,0),(0,1),(0,-1))
        
        while Q:
            d, x, y = heapq.heappop(Q)
            if [x,y]==destination:
                return d
            maze[x][y]='v'
            for i, j in dirs:
                row, col, newd = x, y, d
                while 0<=row+i<m and 0<=col+j<n and maze[row+i][col+j]!=1:
                    row, col, newd = row+i, col+j, newd+1
                if maze[row][col]==0:
                    heapq.heappush(Q, (newd,row,col))
        return -1 #for Maze II
        return 0 #for Maze I
```
Maze III
```
class Solution(object):
    def findShortestWay(self, maze, ball, hole):
        Q = [[0]+ball+['']]
        m = len(maze)
        n = len(maze[0])
        dirs = {(-1,0):'u',(1,0):'d',(0,-1):'l', (0,1):'r'} #m/i direction is up-down, n/j direction is left-right.
        
        paths =[]
        while Q:
            d, x, y, path = heapq.heappop(Q)
            maze[x][y]='v'
            for (i, j), direction in dirs.items():
                nd, nx, ny = d, x, y
                while 0<=nx+i<m and 0<=ny+j<n and maze[nx+i][ny+j]!=1:
                    nd, nx, ny = nd+1, nx+i, ny+j
                    if hole[0]==nx and hole[1]==ny:
                        paths.append( [nd, path+direction])
                        break
                if maze[nx][ny]==0:
                    heapq.heappush(Q, (nd, nx, ny, path+direction))
                    
        return heapq.nsmallest(1, paths)[0][1] if paths else 'impossible'




```
