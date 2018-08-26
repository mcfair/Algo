#brutal force is O(n^2) to check every pairs
#optimal is O(n) for one pass
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height)-1
        water = 0
        while l<r:
            if height[l] < height[r]:
                water = max(water, height[l]*(r-l))
                l +=1
            else:
                water = max(water, height[r]*(r-l))
                r -=1
        return water
