#most difficult part is to find the state transition function
#https://leetcode.com/problems/domino-and-tromino-tiling/discuss/116581/Detail-and-explanation-of-O(n)-solution-why-dpn2*dn-1+dpn-3
        
class Solution(object):
    def numTilings(self, N):
        """
        :type N: int
        :rtype: int
        """
        #f(0) = 1
        #f(1) = 1
        #f(2) = 2
        #f(3) = 5
        #f(4) = 11 
        #f(5) = 24
        #f(n) = 2*f(n-1) +f(n-3)

        f = [0,1,2,5]
        if N<4: return f[N]
        
        f = f + [0]*(N-3)
        for n in range(4,N+1):
            f[n]  = (2* f[n-1]+f[n-3])%1000000007
            
        return f[N]
