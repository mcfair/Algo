#use dfs backtrack will TLE 25/29
class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s==s[::-1]: return 0

        def isvalid(t):
            return t== t[::-1]
        
        def dfs(k, cut):
            if k==len(s):
                self.mincut = min(self.mincut, cut)
                return
            for i in range(k+1,len(s)+1):
                if isvalid(s[k:i] ):
                    if cut+1< self.mincut:
                        dfs(i, cut+1)
                
        self.mincut = float('inf')
        dfs(0, -1)
        return self.mincut


#ask for min number --> consider DP
#state transistion: IF s[i,j] is a palindrome, then the minCut(s[:j]) is at most minCut(s[:i-1])+1.
class Solution(object):
    def minCut(self, s):

        if not s or s==s[::-1]: return 0
        for i in range(1, len(s)):
            if s[:i] == s[:i][::-1] and s[i:] == s[i:][::-1]:
                return 1
         
        #DP array default value is number of chars (every char is a palindrome)
        cut = range(-1,len(s))
        for i in range(0,len(s)):
            for j in range(i,len(s)):
                if s[i:j] == s[j:i:-1]:
                #if s[i:j+1] == s[i:j+1][::-1]: #same effect, but slower...don't know why
                    cut[j+1] = min(cut[j+1],cut[i]+1)
        return cut[len(s)]
