
#O(n^2) time and space
#since the stae transition function only dependent on one previous item, we can do better on space
#dp[i+1][j+1] = dp[i][j] + 1
#need to build the solution diagonally

class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        if not A or not B: 
            return 0
        
        m, n = len(A), len(B)
        
        #Also tried dictionary as data structure, TLE
        dp = [[0]*(m+1) for _ in range(n+1)]
        ret = 0
        for i in range(m):
            for j in range(n):
                if A[i]==B[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                    ret = max(ret, dp[i+1][j+1]) 
        return ret
