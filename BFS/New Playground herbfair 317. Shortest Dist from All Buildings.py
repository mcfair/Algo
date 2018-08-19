#Brutal Force TLE
#to calculate distance first tihing comes to mind is BFS
class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return -1
        m, n = len(grid), len(grid[0])
        
        numBuildings = sum(grid[i][j]==1 for i in range(m) for j in range(n))
        
        minDist = float('inf')
        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:
                    stack = [(i,j)]
                    visited = [(i,j)]
                    count = numBuildings
                    bfsdist, totdist =0, 0
                    while stack:
                        bfsdist +=1
                        nbg = []
                        for x, y in stack:
                            for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                                nx, ny = x+dx, y+dy
                                if 0<=nx<m and 0<=ny<n and grid[nx][ny]!=2 and (nx,ny) not in visited:
                                    if grid[nx][ny] ==1:
                                        count -=1
                                        totdist+=bfsdist
                                    if grid[nx][ny] ==0:
                                        nbg.append((nx, ny))
                                    visited.append((nx,ny))

                        if count==0:
                            minDist = min(totdist, minDist)
                            break
                        stack = nbg
                            
        return minDist if minDist < float('inf') else -1
