"""
Naive way is 2D dp.
Sort it properly (line 13) can convert it to 1D dp (same as Leetcode300.LIS)
"""

class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        if not envelopes: return 0
        envelopes.sort(key= lambda x: (x[0],-x[1]))
        
        n = len(envelopes)
        dp = [1]*n
        for i in range(1,n):
            for j in range(i):
                if envelopes[i][1] > envelopes[j][1]:
                    dp[i] = max(dp[i],dp[j]+1)
        
        return max(dp)
        
        
