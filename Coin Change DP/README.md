```
def permutationSum(self, target, nums):
    #permutation: put target loop outside
    dp = [1] + [0] * target
    for i in range(1, target + 1):
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
```
