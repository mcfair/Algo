#Top down, DFS + Memo
def getMoneyAmount(self, n):
    memo = collections.defaultdict(int)
    def dfs(lo, hi):
        if lo>=hi: 
            return 0
        if (lo,hi) in memo:
            return memo[lo,hi]

        res = float('inf')
        for i in range(lo,hi):
            res = min(res,i + max(dfs(lo,i-1), dfs(i+1, hi)))

        memo[lo,hi] = res
        return res

    return dfs(1,n)
  
 #Bottom up, DP
