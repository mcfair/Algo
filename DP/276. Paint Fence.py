#This is not an easy problem

#use two array/variable to track two states: same, diff
# n, same, diff
# 1, k ,    k
# 2, k ,    k*(k-1)
# 3, k*(k-1), k^2*(k-1)

#can paint "same" only if it was "diff" previously
#can paint "diff" for any condition, so it's "(same+diff)*(k-1)"

class Solution(object):
    def numWays(self, n, k):
 
        if n == 0: return 0
        if n == 1: return k
        
        same, diff = k, k*(k-1)
        for i in range(3, n+1):
            same, diff = diff, (same+diff)*(k-1)
        
        return same+diff
            
