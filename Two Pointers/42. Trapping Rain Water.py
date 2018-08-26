#Start from two ends, the water level of each location 
#depends on min(leftMax, rightMax)
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height)<3: return 0
        
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
