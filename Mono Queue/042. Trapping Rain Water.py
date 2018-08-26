#Method 1, O(n), 32ms DECREASING Mono Queue
#Similar to LC84 Largest Area in Histogram, which store increasing bars in a stack, then calculate area
#This solution uses stack to save decreasing (incl. equal) bars, and then calculate area/water fill.
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        if len(height)<3: 
            return 0
        
        #use stack to store the indices with decreasing wall heights (including equal)
        stack, water = [], 0
        
        for i, h in enumerate(height):
            while stack and h > height[stack[-1]]:
                bottom = stack.pop()
                if stack:
                    level = min(h, height[stack[-1]]) - height[bottom]
                    water += level *(i - stack[-1] -1)
            stack.append(i)
        return water


#Method 2, O(n), 28ms
#Start from two ends, the water level of each location depends on min(leftMax, rightMax)
class Solution(object):
    def trap(self, height):
        
        if len(height)<3: 
            return 0
        
        l, r = 0, len(height)-1
        leftMax = height[l]
        rightMax = height[r]
        water = 0
        while l<r:
            if leftMax < rightMax:
                water += leftMax - height[l]
                l +=1
                leftMax = max(leftMax, height[l])
            else:
                water += rightMax -height[r]
                r -=1
                rightMax = max(rightMax, height[r])
        return water
