class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        one = collections.defaultdict(int)
        one.update({str(i): 1 for i in range(1,10)})
        
        two = collections.defaultdict(int)
        two.update({str(i): 1 for i in range(10,27)})
        
        prev, cur = 1, one[s[0]]
        
        for i in range(1, len(s)):
            prev, cur = cur, cur*one[s[i]] + prev*two[s[i-1:i+1]]
            
        return cur
