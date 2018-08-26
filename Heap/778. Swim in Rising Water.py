""" 
Heap: 60 ms,  O(mnlog(mn))
Always swin into the smallest number that is 4-directionally adjacent to the ones we've visited.
Keep a priority queue of which position we can walk in next. 
When we reach the target, answer(waited time) is the largest number we've visited.
"""

class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        seen = set([])
        pq = [(grid[0][0],0,0)]
        ans = grid[0][0]
        
        while pq:
            t, i, j = heapq.heappop(pq)
            ans = max(ans, t)
            if i==m-1 and j==n-1: 
                return ans  
            for x, y in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
                if 0<=x<m and 0<=y<n and (x,y) not in seen:
                    heapq.heappush(pq, (grid[x][y], x, y))
                    seen.add((x,y))
        return -1

    
"""
Union Find: 140ms, O(mn)
with path compression, the time complexity should be O(n^2*alpha(n^2)), where alpha is inverse Ackermann function, 
which is small and can be regarded as a constant. So it is fair to say the time complexity is O(n^2) or O(mn).

idea:
go through the grid by the order of its value grid[i][j] 
increment time and union its reachable neighbours (grid[i][j] < t)
"""
class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid)  , len(grid[0])
        self.papa = { }
        self.rank = collections.defaultdict(int)
        
        pos = {}
        for i in range(m):
            for j in range(n):
                pos[grid[i][j]] = (i,j)
        
        for t in range(m*n): #count the clock, access 
            i,j = pos[t]
            for x, y in ((i+1,j),(i-1,j),(i,j-1),(i,j+1)): #union its reachable neighbours
                if 0<=x<m and 0<=y<n:
                    if grid[x][y]< t: 
                        self.union((i,j),(x,y))
                        if self.find((0,0))==self.find((m-1,n-1)):
                            return t
        return -1
        
    def find(self, x): #find with path compression
        if x not in self.papa:
            self.papa[x] = x
        while self.papa[x] !=x:
            x, self.papa[x] = self.papa[x], self.papa[self.papa[x]]
        return x
    
    def union(self, x,y): #union by rank  - "without rank, it will be TLE"
        x, y = self.find(x), self.find(y)
        if x!=y:
            if self.rank[x] > self.rank[y]:
                self.papa[y] = x
            elif self.rank[x] < self.rank[y]:
                self.papa[x] = y
            else:
                self.papa[y] = x
                self.rank[x] +=1
                
    
    
