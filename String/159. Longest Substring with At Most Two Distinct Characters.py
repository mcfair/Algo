
class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s, k=2):
        """
        :type s: str
        :rtype: int
        """
        if len(s)<=2: return len(s)
        
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
        
