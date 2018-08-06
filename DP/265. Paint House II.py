#min cost is apparently a DP 
#looks like this DP requires a cost as well as a state to avoid identical color adjacently
#R[0] = costs[0][0]
#G[0] = costs[0][1]
#B[0] = costs[0][2]
#R[1] = min( G[0], B[0]) +costs[1][2]

#O(n^2) time and O(n^2) space
class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        
        if not costs or not costs[0]: 
            return 0
        
        n, k = len(costs), len(costs[0])
        
        dp = costs[:]
        for i in range(1,n):
            for j in range(k):
                #dp[i][j] = costs[i][j] + min(dp[i-1][:j] + dp[i-1][j+1:])
                dp[i][j] += min(dp[i-1][:j] + dp[i-1][j+1:])
        
        return min(dp[n-1])
    
        
 #O(n^2) time and O(1) space    
 class Solution(object):
    def minCostII(self, costs):
        if not costs or not costs[0]: 
            return 0
        
        n, k = len(costs), len(costs[0])
     
        for i in range(1,n):
            for j in range(k):
                costs[i][j] += min(costs[i-1][:j] + costs[i-1][j+1:])
        
        return min(costs[n-1])
    
