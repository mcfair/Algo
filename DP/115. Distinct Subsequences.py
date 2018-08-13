#O(n)space
class Solution(object):
    def numDistinct(self, s, t): 
        #empty string is always a subsquence of any string 
        prev = [1]*(len(s)+1)
        
        #go row by row
        for i in range(len(t)):
            dp = [0]*(len(s)+1)
            for j in range(len(s)):
                if t[i]==s[j]:
                    dp[j+1] = dp[j] + prev[j]
                else:
                    dp[j+1] = dp[j]
            prev = dp
        
        return dp[len(s)]
                
                
#O(mn)space                
class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        #count numbers is typically DP
        #
                            
        dp = collections.defaultdict(int)
        
        # -1 represents empty target string t=''
        for j in range(-1,len(s)):
            dp[-1, j] = 1
        
        for i in range(len(t)):
            for j in range(len(s)):
                if t[i]==s[j]:
                    dp[i,j] = dp[i,j-1] + dp[i-1,j-1]
                else:
                    dp[i,j] = dp[i,j-1]
                    
        return dp[len(t)-1,len(s)-1]
                
