#standard two pointers
"""
Track two pointers and majority_count
"""
def characterReplacement(self, s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """  
    count = collections.Counter()
    start = result = 0
    for end in range(len(s)):
        count[s[end]] += 1
        #majority_count = count.most_common(1)[0][1]
        majority_count = max(majority_count, count[s[end]])  # 140ms with this line, compared to 400ms with line above.
        #if end - start + 1 > majority_count + k:
        while end - start + 1 > majority_count + k: # "while" is more readable, but "if" works as well.
            count[s[start]] -= 1
            start += 1
        result = max(result, end - start + 1)
    return result
  
#method 2 - less readable
"""
Keep track of curlen, end and majority_count
"""
def characterReplacement(self, s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """ 
    majority = curlen = 0
    count = collections.Counter()
    for j in range(len(s)):
        count[s[j]] += 1
        majority = max(majority, count[s[j]])
        if curlen - majority < k: 
            curlen += 1
        else: 
            # start = j - curlen
            count[s[j - curlen]] -= 1
    return curlen
