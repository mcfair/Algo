class Solution(object):
    def shortestDistance(self, grid):

        if not grid or not grid[0]: return -1
        
        m, n = len(grid), len(grid[0])
        
        buildings = []
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    buildings.append((i,j))
        totalB = len(buildings)
        dist = [[0]*n for _ in range(m)]
        ## do BFS from each building, and decrement all empty place for every building visit
        ## when grid[i][j] == -totalB, it means that grid[i][j] are already visited from all buildings
        ## and use dist to record distances from buildings
        ## if certain cells can't reach all buildings, then the total dist shouldn't count.
        def bfs(i, j, bIndex):
            """walking from the bulding"""
            queue = collections.deque([(i, j, 0)])
            while queue:
                i, j, d = queue.popleft()
                for x,y in [(i+1, j), (i-1, j), (i, j-1), (i, j+1)]:
                    if 0<=x<m and 0<=y<n and grid[x][y]==bIndex:
                        dist[x][y] += d+1
                        grid[x][y] -= 1
                        queue.append((x, y, d+1))

        bIndex = 0
        for i, j in buildings:
            bfs(i, j, bIndex)
            bIndex -= 1
        res = [dist[i][j] for i in range(m) for j in range(n) if grid[i][j]+totalB==0]
        return min(res) if res else -1


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
