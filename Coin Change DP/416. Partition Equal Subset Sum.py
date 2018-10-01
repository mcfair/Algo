#convert to 0-1 coin change problem: use each coin only once to make a change of B
        
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        S = sum(nums)
        if S%2: return False
        B = S/2

        dp = [1]+[0]*B
        for x in nums:
            for b in range(B, x-1, -1):
                dp[b] = dp[b-x] or dp[b]
         
        return bool(dp[B])
            
