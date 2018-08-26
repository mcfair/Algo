```
#save all steps of all possible paths
class Solution(object):
    def shortestDistance(self, maze, start, destination):
 
        Q = [[0]+start]
        m, n = len(maze), len(maze[0])
        dirs = ((1,0),(-1,0),(0,1),(0,-1))
        
        steps=[]
        while Q:
            d, x, y = heapq.heappop(Q)
            if [x,y]==destination:
                steps.append(d)
                continue
            maze[x][y]='v'
            for i, j in dirs:
                row, col, newd = x, y, d
                while 0<=row+i<m and 0<=col+j<n and maze[row+i][col+j]!=1:
                    row, col, newd = row+i, col+j, newd+1
                if maze[row][col]==0:
                    heapq.heappush(Q, (newd,row,col))
                    
return -1 if not steps else min(steps)

```
