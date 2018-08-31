"""
two cases:
when there are less than k chars in the hash table we put the char in the hash table
when there are exactly distinct k chars in the hash table and we need to add a new char, we delete the left most char
"""
class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if k == 0:
            return 0
        start = 0
        char_hash = {}
        max_len = 0
        for char in s:
            if len(char_hash) < k:
                if char not in char_hash:
                    char_hash[char] = 1
                else:
                    char_hash[char] += 1
            elif len(char_hash) == k:
                if char not in char_hash:
                    max_len = max(max_len, sum(char_hash.values()))
                    while len(char_hash) == k:
                        char_hash[s[start]] -= 1
                        if char_hash[s[start]] == 0:
                            del char_hash[s[start]]
                        start += 1
                    char_hash[char] = 1
                else:
                    char_hash[char] += 1
        max_len = max(max_len, sum(char_hash.values()))
        return max_len
