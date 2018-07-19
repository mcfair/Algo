class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
     
        l, r = 0, len(s)-1
        while l<=r :
            if s[l]==s[r]:
                l, r = l+1, r-1
            else:
                #exclude r or exclude l
                return self.isValid(s[l:r]) or self.isValid(s[l+1:r+1])
      
        return True
    
    def isValid(self,s):
        return s==s[::-1]
    
    def isValid2(self,s):
        l, r = 0, len(s)-1
        while l<=r :
            if s[l]==s[r]:
                l, r = l+1, r-1
            else:
                return False
        return True
