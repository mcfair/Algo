
def lengthOfLongestSubstringKDistinct(self, s, k):
        if not s:
            return 0
        if k >= len(s):
            return len(s)
        if k == 0:
            return 0
        
        dic = {}
        
        count = 0
        l = 0
        r = 0
        s = list(s)
        maxCount = 0
        
        # O(n) time
        while r < len(s):
            # If character not in dic then we add it and increment a count
            if s[r] not in dic:
                dic[s[r]] = 1
                count += 1
            else:
                dic[s[r]] += 1
                
            # We reached the max distinct characters, update maxCount
            if count <= k:
                maxCount = max(maxCount, r-l+1)

            # If count is greater than k then we have to shrink the window
            else:
				# check if l is in the dic, if so we have to decrement it
				# and if it is now decremented to 0, we remove that from the dic
				# and reduce count by 1
                if s[l] in dic:
                    dic[s[l]] -= 1
                    if dic[s[l]] == 0:
                        del dic[s[l]]
                        count -= 1
                l += 1
            r += 1

        return maxCount
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
