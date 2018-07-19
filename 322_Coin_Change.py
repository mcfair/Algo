class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        #unlimited coin change
        #need[b] := #of coins to make a change 'b'
        
        need =[0] + [float('inf')]*amount
        
        for c in coins:
            for b in range(c, amount+1): 
                need[b] = min(need[b], need[b-c]+1)
        
        return need[amount] if need[amount] < float('inf') else -1
        
 
