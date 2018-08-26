#ask for min number --> DP
#state transistion: IF s[i,j] is a palindrome, then the minCut(s[:j]) is at most minCut(s[:i-1])+1.
class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
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
