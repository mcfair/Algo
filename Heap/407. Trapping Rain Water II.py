"""
Idea is the same as the two pointer solution of Trapping Rain Water I.
In a 1-D array, we only need to compare two pointers to find the lower boundary, 
In a 2-D array, we have more candidate pointers to choose from, so a heap can help us to always pick the shortest panel, 
and a visited set can help us exclude visited points.
https://www.youtube.com/watch?v=cJayBq38VYw&t=195s

Imagine a case with 3x3 array
5 8 9
3 1 2
4 7 6
Push all edge cells to heap as initial boundaries. 
According to Wooden Bucket Theory, the effective boundary is determined by its shortest panel 2.
Use heap to pop out the minPanel, water = max(0, minPanel - centerHeight)
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
            minPanel, i, j = heapq.heappop(q)
            for x,y in ((i+1,j),(i-1,j),(i,j-1),(i,j+1)):
                if 0<=x<m and 0<=y<n and (x,y) not in visited:
                    water += max(0, minPanel - h[x][y])
                    heapq.heappush(q,(max(h[x][y], minPanel), x, y))
                    visited[x,y] = 1
        return water
