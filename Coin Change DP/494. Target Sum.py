#https://leetcode.com/problems/target-sum/description/

class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        #sum(P) + sum(N) = sum(nums)
        #sum(P) - sum(N) = S 
        #2*sum(P) = S + sum(nums)
        #problem reduces to coin change # of ways, use only once
        #target = (S + sum(nums))/2
        
        if not nums: return 0
        sums = sum(nums)
        target, mod = divmod(S + sums, 2)
        if mod==1 or S > sums: return 0
        
        dp = [1]+[0]*target
        for c in nums:
            for i in range(target, c-1, -1):
                dp[i] += dp[i-c]
        return dp[target]
 
        
        
