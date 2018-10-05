"""
The problem depends not only on a state, but two states (the largest and smallest products).
dp[i] only depends on dp[i - 1] so we can optimize for space by saving only one step backwards.
"""
def maxProduct(self,a):
    imin = imax = res = a[0]
    for i in range(1,len(a)):
        if a[i] < 0:
          imax, imin = imin, imax
        imax = max(a[i], imax*a[i])
        imin = min(a[i], imin*a[i])
        res = max(imax, res)
        
     return res
        
  
