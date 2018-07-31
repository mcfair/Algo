#this is not optimal. Optimal solution is O(n)
class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s: return ''
        
        for c in sorted(set(s)):   #sort the char because we need to return lexicographical order
            suffix = s[s.index(c):]
            if set(suffix) == set(s): #this condition means "without losing any char after c"
                return c + self.removeDuplicateLetters(suffix.replace(c, ''))
         
        
