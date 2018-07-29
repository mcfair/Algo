#Basic idea: the opponent can't win the next round
#Vanilla form, 2086ms
class Solution(object):        
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        for i in range(len(s)-1):
            if s[i:i+2]=='++':
                nextstate = s[:i]+ '--' +s[i+2:]
                if not self.canWin(nextstate):
                    return True
        return False

#Use memorization, 76ms
class Solution(object):
    def __init__(self):
        self.memo = {}
        
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 1-liner, slower than for-loop
        if s not in self.memo:
            self.memo[s] = any(not self.canWin(s[:i]+"--"+s[i+2:]) 
                                for i in xrange(len(s)-1) if s[i:i+2] == "++")
        return self.memo[s]
    

