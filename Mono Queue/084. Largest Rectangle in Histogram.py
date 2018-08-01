#Mono stack: keep track of increasing bars
class Solution(object):
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
            else: #when height[i] >= height in stack
                stack.append(i)
        height.pop()
        return maxa
        
        
     
 class Solution(object):
     def maxRecArea(self, heights):
        #LeetCode084, O(n) 44ms
        #High level idea is to find the max spread of each bar
  
        n = len(heights)
         
        L = range(n)
        for i in range(1,n):
            l = i-1
            while l>=0 and heights[l] >= heights[i]:
                L[i] = L[l] 
                l = L[l] - 1
            
            
        R = range(n)
        for i in range(n-2,-1,-1):
            r = i+1
            while r<n and heights[r] >= heights[i]:
                R[i] = R[r]
                r = R[i] + 1 
        
        maxa =0
        for i in range(n):
            area = (R[i]-L[i]+1)*heights[i]
            maxa = max(area, maxa)
        return maxa
            
            
