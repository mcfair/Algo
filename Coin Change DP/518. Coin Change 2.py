#coin change variant: unlimited, # of ways
#dp[i]:= number of ways given nums[:i]
class Solution(object):
    def change(self, target, nums):
        """
        :type target: int
        :type coins: List[int]
        :rtype: int
        """ 

        dp = [1]+[0 for _ in range(target)]
        for x in nums:
            for b in range(x, 1+target):
                dp[b] += dp[b-x]
                
        return dp[target]
