#Top down, DFS + Memo
def getMoneyAmount(self, n):
    memo = {}
    def dfs(lo, hi):
        if lo>=hi: 
            return 0
        if (lo,hi) in memo:
            return memo[lo,hi]

        res = float('inf')
        #take "i" that cost the least
        #for each choice of i, the cost = max(dfs(lo,i-1)+i, dfs(i+1, hi)+i)
        for i in range(lo,hi):
            res = min(res, i + max(dfs(lo,i-1), dfs(i+1, hi)))
            
        memo[lo,hi] = res
        return res

    return dfs(1,n)
  
 #Bottom up, DP
