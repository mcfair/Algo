#Hard

class Solution(object):
    def largestRectangleArea1(self, height):
        """
        :type heights: List[int]
        :rtype: int
        """
        #Method 1,  O(n) 44ms
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
                l = L[l] -1 #skipping steps, instead of using l-=1
             
        
        R = range(n+2) # right boundary
        maxa = 0
        for i in range(n,0, -1):
            r = i+1
            while height[i] <= height[r]:
                R[i] = R[r]
                r = R[r] +1 # skipping steps, instead of using r+=1
            w = R[i]-L[i]+1
            maxa = max(maxa, w*height[i])  
                
        return maxa
    
    def largestRectangleArea2(self, height):
        #high level idea is the same as method 1: find the max spread of each bar
        #we can use a stack to store left index
        
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
