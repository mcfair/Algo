class Solution(object):
    def largestRectangleArea(self, height):
        """
        :type heights: List[int]
        :rtype: int
        """
    
        #Basic idea:
        #First step, find the max spread (w) of each bar with its height (height[i]) shrehold, 
        #Second step, take the max of w[i]*height[i] for all i
        #Naive method would take O(n^2). For each i, it may take up to O(n) to find w[i]
        
        #44ms O(n)
        if not height: return 0
        n = len(height)
        
        height = [-1] + height +[-1]
        
        L = range(n+2) #left boundary
        for i in range(1,n+1):
            l = i-1
            while height[i] <= height[l]:
                L[i] = L[l]
                l = L[i] -1 #skipping steps, instead of using l-=1
             
        
        R = range(n+2) # right boundary
        maxa = 0
        for i in range(n,0, -1):
            r = i+1
            while height[i] <= height[r]:
                R[i] = R[r]
                r = R[i] +1 # skipping steps, instead of using r+=1
            w = R[i]-L[i]+1
            maxa = max(maxa, w*height[i])  
                
        return maxa
