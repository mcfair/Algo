"""
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
