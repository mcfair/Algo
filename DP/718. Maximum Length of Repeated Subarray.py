
#O(n^2) time and space
#since the stae transition function only dependent on one previous item, we can do better on space
#dp[i+1][j+1] = dp[i][j] + 1
#only need to keep one row of dp matrix.
#Further step is to use O(1) space if we can build dp solution diagonally
#with space optmization time got reduced too
#2630ms -> 2370ms -> 1700ms 

#Another follow up is return the subarray itself.

#O(n^2) space
class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        if not A or not B: 
            return 0
        
        m, n, ret = len(A), len(B), 0
        
        #Also tried dictionary as data structure, TLE
        dp = [[0]*(m+1) for _ in range(n+1)]
         
        for i in range(m):
            for j in range(n):
                if A[i]==B[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                    ret = max(ret, dp[i+1][j+1]) 
        return ret


#O(n) space, build DP solution row by row
class Solution(object):
    def findLength(self, A, B):
 
        if not A or not B: 
            return 0
        
        m, n, ret = len(A), len(B), 0

        dp = [0]*(n+1)
        for i in range(m):
            for j in range(n-1 , -1, -1):
                if A[i]==B[j]:
                    dp[j+1]  = dp[j] + 1
                    ret = max(ret, dp[j+1] ) 
                else:   #need to reset to zero in 1D array because of space reuse!
                    dp[j+1] =0
      
        return ret
 
#O(1) space, build DP solution diagonally
class Solution(object):
    def findLength(self, A, B):
 
        if not A or not B: 
            return 0
        
        m, n , ret = len(A), len(B), 0
         
        for i in range(m):
            prev = 0
            for k in range(m-i):
                if A[k+i] == B[k]:
                    prev +=1
                    ret = max(ret, prev)
                else:
                    prev =0 #Remember to reset! because of space reuse
                    
        for j in range(1,n):
            prev = 0
            for k in range(n-j):
                if A[k]==B[k+j]:
                    prev+=1                  
                    ret = max(ret, prev)
                else: 
                    prev =0 #Remember to reset! because of space reuse
        return ret
                
