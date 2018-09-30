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
