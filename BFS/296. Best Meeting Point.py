#TLE at 56/57 test cases
class Solution(object):
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]: 
            return None
        m, n = len(grid), len(grid[0])
        
        def bfs(i,j):
            q = collections.deque([(i,j, 0)])
            while q: 
                i, j, d = q.popleft()
                dist[i][j] += d
                for x, y in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                    if 0<=x<m and 0<=y<n and (x,y) not in visited:
                        visited.add((x,y))
                        q.append((x,y,d+1))
                        
        dist = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1: 
                    visited = set([(i,j)])
                    bfs(i,j)
        
        return min(map(min,dist))
