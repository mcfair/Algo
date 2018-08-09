
#idea is to find max hisgoram for row[0~i]
class Solution(object):
    def maximalRectangle(self, matrix):
        
        if not matrix or not matrix[0]: 
            return 0
        
        n = len(matrix[0])
        prev = [0]*n
        
        maxa = 0
        for row in matrix:
            heights = [int(row[i])*(1+prev[i]) for i in range(n)]
            maxa = max(maxa, self.maxHistogram(heights))
            prev = heights
        return maxa
        
    def maxHistogram(self, heights):
        n = len(heights)
        L = [0]*n
        R = [0]*(n-1)+ [n-1]
        for i in range(1,n):
            L[i] = i if heights[L[i-1]] < heights[i] else L[i-1]
            
        for i in range(n-2,-1,-1):
            R[i] = i if heights[R[i+1]] < heights[i] else R[i-1]
        
        maxa =0
        for i in range(n):
            area = (R[i]-L[i]+1)*heights[i]
            maxa = max(area, maxa)
        return maxa
            
#naive solution is O(n^4) 2D range sum
#use solution to largest are of histogram

class Solution(object):
    def maximalRectangle2(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        m = len(matrix)
        n = len(matrix[0])
        rsum = collections.defaultdict(int)
        
        for i, row in enumerate(matrix):
            for j in range(len(row)):
                rsum[i,j] = rsum[i-1,j] + rsum[i,j-1] - rsum[i-1,j-1] + int(matrix[i][j])
        
        maxrec = 0
        for i in range(m):
            for j in range(n):
                for h in range(m-i):
                    for w in range(n-j):    
                        area = (h+1)*(w+1)
                        sums = rsum[i+h,j+w] - rsum[i+h,j-1] - rsum[i-1, j+w] + rsum[i-1,j-1]
                        if area == sums:
                            maxrec = max(maxrec, area)
                            
        return maxrec
                        
                        
                        
 
        
