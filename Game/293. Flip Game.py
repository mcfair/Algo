#1-liner
class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        return [s[:i]+'--'+s[i+2:] for i in range(len(s)-1) if s[i:i+2]=='++']

#Verbose
class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans = []
        for i in range(len(s)-1):
            if s[i:i+2]=='++':
                ans.append(s[:i]+'--'+s[i+2:])
        return ans
