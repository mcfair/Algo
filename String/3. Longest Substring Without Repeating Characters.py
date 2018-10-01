 
def lengthOfLongestSubstring(self, s):
    """
    :type s: str
    :rtype: int
    """
    if not s: return 0

    ans, i = 1, 0
    s = s +'#'
    hashset = set(['#'])
    for j, c in enumerate(s):
        if c in hashset:
            ans = max(ans, j-i)
            while i<j and c in hashset and s[i] in hashset:
                hashset.remove(s[i])
                i +=1
        hashset.add(c)

    return  max(ans, j-i)          



