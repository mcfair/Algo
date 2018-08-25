# DP
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = collections.defaultdict(int)
        dp[0,0] = 1
        
        m, n = len(s), len(p)
        for j in range(n):
            if p[j]=='*' and dp[0,j]:
                dp[0,j+1]=1
        
        for i in range(m):
            for j in range(n):
                if p[j] in {s[i],'?'}:
                    dp[i+1,j+1] = dp[i,j]
                elif p[j]=='*':
                    dp[i+1,j+1] = dp[i,j+1] or dp[i+1,j]
                
        return  bool(dp[m,n])
        
# recursion + memorization
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        
        s_len, p_len = len(s), len(p)
        memo = {}
        def backtrack(i, j):
            # i is index in s and j is index in p
            key = (i, j)
            if key in memo: 
                return memo[key]
            
            if j == p_len: 
                ans = i == s_len
            elif i == s_len: 
                ans = j == p_len or  p[j:].count('*')==len(p[j:])
            else:    
                first_match = p[j] in {s[i], '*', '?'}    
                if p[j] == '*':
                    # either match nothing, or match current char and move on
                    ans = backtrack(i, j+1) or backtrack(i+1, j)
                else:
                    ans = first_match and backtrack(i+1, j+1)    
            memo[key] = ans    
            return ans   
        return backtrack(i=0, j=0)
