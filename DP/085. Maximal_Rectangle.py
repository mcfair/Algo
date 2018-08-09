
#idea is to find max hisgoram for row[0~i]
#O(nm) 
class Solution(object):
    def maximalRectangle(self, matrix):
 
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        #if m==n==1: return int(matrix[0][0])
        
        prev, maxa = [0]*n, 0
        for row in matrix:
            height = [int(row[i])*(1+prev[i]) for i in range(n)]
            maxa = max(self.maxRecArea(height), maxa)
            prev = height
            
        return maxa
    
    
    def maxRecArea(self, heights):
        #LeetCode084, O(n) 44ms
        #High level idea is to find the max spread of each bar
        n = len(heights)
         
        L = range(n) #index of left boundary for each position
        for i in range(1,n):
            l = i-1
            while l>=0 and heights[l] >= heights[i]:
                L[i] = L[l] 
                l = L[i] - 1 
                #L[i] is the leftest index that < heights[i]
                

        R = range(n) #index of right highest for each position
        for i in range(n-2,-1,-1):
            r = i+1
            while r<n and heights[r] >= heights[i]:
                R[i] = R[r]
                r = R[i] + 1 
                #R[i] is the rightest index that < heights[i]
                
        maxa =0
        for i in range(n):
            area = (R[i]-L[i]+1)*heights[i]
            maxa = max(area, maxa)
        return maxa
    
    def maxRecArea2(self, height):
        #LeetCode084, O(n) 44ms
        #High level idea is to find the max spread of each bar
        #we can use a mono stack to store INCREASING indices, which is the left buondary
        #and right boundary is when we see a drop h[i] < h[i-1]
        
        height.append(-1)
        stack, maxa = [-1], 0
        
        for i in range(len(height)):
            while height[i] < height[stack[-1]]:
                # "<" condition finds the right boundary "i-1" for all bars in the stack
                # left boundary is the index in the stack 
                h = height[stack.pop()]
                l, r = stack[-1], i-1
                w = r-l
                maxa = max(maxa, h*w)           
            else:
                stack.append(i)
        
        height.pop()
        return maxa
#naive solution is O(n^2*m^2) 2D range sum
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
                        
                        
                        
 
        
