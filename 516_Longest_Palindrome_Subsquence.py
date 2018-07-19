

#standard O(n^2) time O(n^2) space solution, 1800ms
class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        #dp [i,j]:= LPS in s[i:j+1]
        
        #first check if it's palindrome string
        if s[::-1]==s: return len(s) #critical to pass OJ
        
        #standard DP using dict      
        dp = collections.defaultdict(int)
        for i in range(len(s)):
            dp[i,i] = 1
        for i in range(len(s)-1):
            dp[i,i+1] = 2 if s[i]==s[i+1] else 1
        
        for lens in range(3,len(s)+1):
            for i in range(len(s) - lens +1):
                j = i + lens -1
                if s[i]==s[j]:
                    dp[i, j] = 2 + dp[i+1,j-1]
                else:
                    dp[i, j] = max(dp[i,j-1], dp[i+1, j])
                    
        return dp[0,len(s)-1]
            
