"""
The first loop check sto see if we have enough '(' and '*' characters to balance out the ')' character. 
If balance ==0 (var cnt in code below), it's already satisified, return True.
If balance > 0, it means we have more than enough '('.

The second loop checks to see if we have enough ')' and '*' to balance out the '(' character

The first and second loop logic combine together and say we have enough '(', ')', '*' character 
to balance out both the '(' and ')' parens.
"""
class Solution(object): 
    def checkValidString(self, s):
        cnt =0 
        for c in s:
            if c in '(*': cnt +=1
            if c ==')':   cnt -=1
            if cnt < 0:   return False
        
        if cnt ==0: 
            return True
        else:
            cnt =0
            
        for c in s[::-1]:
            if c in ')*': cnt +=1
            if c =='(':   cnt -=1
            if cnt < 0:   return False
        
        return True
    
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
        
            
            
