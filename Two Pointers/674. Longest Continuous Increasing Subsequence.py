class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        
        l = r = 0
        ans = 1
        for i in range(1,len(nums)):
            if nums[i] > nums[r]:
                r += 1
            else:
                ans = max(ans, r-l +1)
                l = r = i
        
        return max(ans, r-l+1)
            
