 class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """  
        if k==0 or not s: return 0
       
        dic = {}
        i = ans = 0
        for j, c in enumerate(s):
            if len(dic) == k  and c not in dic:
                ans = max(ans, j-i)
                while i<j and len(dic)==k:
                    if dic[s[i]]==i:
                        del dic[s[i]]
                    i+=1
                
            dic[c] = j
               
       
        return max(ans, j-i+1)
