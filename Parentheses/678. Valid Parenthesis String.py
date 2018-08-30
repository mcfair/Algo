
#TLE -DFS
class Solution(object): 
    def isValid(self,s):
        if len(s)%2!=0:
            return False
        cnt = 0
        for c in s:
            if cnt < 0: 
                return False
            if c =='(':
                cnt +=1
            if c ==')':
                cnt -=1
        return cnt==0
                
    def checkValidString(self, s):
        if s.count('*')==0:
            return self.isValid(s.strip())
        for i, c in enumerate(s):
            if c=='*':
                p1 = self.checkValidString(s[:i]+s[i+1:]) 
                p2 = self.checkValidString(s[:i]+'('+s[i+1:]) 
                p3 = self.checkValidString(s[:i]+')'+s[i+1:])
                return p1 or p2 or p3
        
            
            
