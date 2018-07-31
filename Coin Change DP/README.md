```
# number of ways - unlimited coins - permutation: put amount loop outside
def permutationSum(self, target, nums):

    dp = [1] + [0] * target
    for i in range(1, target + 1):
        for c in nums:
            if i>=c:
                dp[i]+=dp[i-c]
    return dp[target]

# number of ways - unlimited coins - combination: put amount loop inside
def combinationSum(self, target, nums):
    
    dp = [1]+[0]*target
    for c in nums:
        for i in range(c, 1+target):
            dp[i] += dp[i-c]
    return dp[target]

# min number of coins - unlimited coins - put amount loop inside
def coinChange(self, coins, amount):
 
    dp = [0]+[float('inf')]*amount
    for c in coins:
        for i in range(c, amount+1):
                dp[i] = min(dp[i], dp[i-c]+1)
    return dp[amount] if dp[amount] < float('inf') else -1


```
