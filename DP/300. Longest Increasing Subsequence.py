#O(n^2)
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        
        dp = [1]*len(nums)
        
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j]<nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
                    
        return max(dp)
    
#O(nlogn) Binary Search
import bisect
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0]*len(nums)
        l = 0
        for num in nums:
            i = bisect.bisect_left(dp, num, 0, l)
            dp[i] = num
            if i == l:
                l+=1
        return l
