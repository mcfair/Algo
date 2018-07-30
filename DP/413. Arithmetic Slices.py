#MLE - use too much space
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

# from the MLE solution above, we can reduce space complexity
# observe state transition function, current state only depends on one previous state j-1
# so we only need two variables: prev and curr to store state transition info.
class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        #sound like a DP
    
        ans = 0
        for lens in range(3, len(A)+1):
            for i in range(0, len(A)+1 - lens):
                j = i+lens -1
                if lens==3:
                    prev = A[j]+A[j-2]==A[j-1]*2
                else:
                    if prev and A[j]+A[j-2]==A[j-1]*2:
                        curr = True
                    else:
                        curr = False
                    prev = curr
                ans += prev
        return ans
    
