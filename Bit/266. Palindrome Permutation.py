"""
bit XOR ^ operator to toggle 0, 1
odd counts = 1
even counts = 0
"""
class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        counter = collections.defaultdict(int)
        for c in s:
            counter[c] ^=1  
        
        return sum(counter.values()) < 2
