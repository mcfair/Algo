class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        #coin change, unlimited, min # of coins 
        dp = [0]+[float('inf')]*amount
        
        for c in coins:
            for i in range(c, amount+1):
                    dp[i] = min(dp[i], dp[i-c]+1)
        
        return dp[amount] if dp[amount] < float('inf') else -1
                
