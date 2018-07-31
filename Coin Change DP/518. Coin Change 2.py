#coin change variant: unlimited, # of ways
#dp[i]:= number of ways given nums[:i]
class Solution(object):
    def change(self, target, nums):
        """
        :type target: int
        :type coins: List[int]
        :rtype: int
        """ 

        dp = [1]+[0]*target
        for x in nums:
            for b in range(x, 1+target):
                dp[b] += dp[b-x]
                
        return dp[target]

    
    
    def permutationSum(self, target, nums):
        #permutation: put target loop outside
        dp = [1] + [0] * target
        for i in range(1, target + 1):
            #dp[i] = sum([dp[i - c] for c in nums if i >= c])
            for c in nums:
                if i>=c:
                    dp[i]+=dp[i-c]
        return dp[target]
    
    def combinationSum(self, target, nums):
        #combination: put target loop inside
        dp = [1]+[0]*target
        for c in nums:
            for i in range(c, 1+target):
                dp[i] += dp[i-c]
        return dp[target]
