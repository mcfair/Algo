#DFS + Memo
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)
        if n - p.count('*') > m:
            return False
        
        memo = {}  
        def check(i,j):
            if (i,j) in memo: 
                return memo[i,j]
            if j==n:
                ans= i==m
            elif i==m:
                ans= j==n or p[j:]=='*'*(n-j)
            elif p[j] in {s[i],'?'}:
                ans= check(i+1,j+1)
            elif p[j]=='*':
                ans= check(i+1,j) or check(i,j+1)
            else:
                ans=False
            memo[i,j]=ans
            return ans
        
        return check(i=0,j=0)
