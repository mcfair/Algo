"""
Idea is the same as the two pointer solution of Trapping Rain Water I, the difference is that in a 1-D array, there are always two pointers to choose from and we only need to compare two pointers to know when to stop, but in a 2-D array, we have more candidate pointers to choose from, so a heap can help us, and a visited set can help us exclude visited points and check when to stop.
https://www.youtube.com/watch?v=cJayBq38VYw&t=195s

Imagine a case with 3x3 array
5 8 9
3 1 2
4 7 6
Push all bounary cells to heap. According to Wooden Bucket Theory, the effective boundary is determined by its min boundary 2.
Use heap to pop out the minBoundary, water = max(0, minBoundary - centerHeight)
"""
class Solution(object):
    def trapRainWater(self, h):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        if not h or not h[0]: return 0
        m, n = len(h ), len(h[0])
        if m<3 or n<3: return 0
        
        visited = { }
        water = 0
        q = []
        
        #bounary cells are the planks of the water bucket
        for i in range(m):
            for j in range(n):
                if i==0 or i==m-1 or j==0 or j==n-1:
                    heapq.heappush(q, (h[i][j],i,j))
                    visited[i,j] = 1
        
        #shortest plank always determines the water amount
        while q:
            shortestPlank, i, j = heapq.heappop(q)
            for x,y in ((i+1,j),(i-1,j),(i,j-1),(i,j+1)):
                if 0<=x<m and 0<=y<n and (x,y) not in visited:
                    water += max(0, shortestPlank - h[x][y])
                    heapq.heappush(q,(max(h[x][y], shortestPlank), x, y))
                    visited[x,y] = 1
        return water
