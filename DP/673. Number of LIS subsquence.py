"""
Double DP 
dp to store max len of LIS ending at i
cnt to keep track of how many occurence max len LIS for each i
"""
class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        
        dp = [1]*len(nums)
        cnt= [1]*len(nums)
        
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[j]+1 > dp[i]: 
                        dp[i] = dp[j] +1
                        cnt[i] = cnt[j]
                    elif dp[j]+1 == dp[i]: 
                        cnt[i] += cnt[j]
        
        return sum(cnt[i] for i in range(len(nums)) if dp[i]==max(dp))
