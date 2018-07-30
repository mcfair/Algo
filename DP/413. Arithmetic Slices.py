#MLE
class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        #sound like a DP
        #DP[i,j] denotes whether or not A[i,j] is arithmetic list
        
        dp = collections.defaultdict(bool) #default bool = False
        
        for i in range(len(A)-2):
            if A[i] + A[i+2]==A[i+1]*2:
                dp[i, i+2] = True
       
        for lens in range(4, len(A)+1):
           
            for i in range(0, len(A)+1 - lens):
                j = i+lens -1
           
                if dp[i,j-1]  and A[j]+A[j-2]==A[j-1]*2:
                    dp[i,j]=True
        
        return sum(dp.values())
    
