#use set
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


 
 #use dict to store index, allow i to directly jump to new eligible start
 def lengthOfLongestSubstring(self, s):
     if not s: return 0
     ans = i = 0
     occur = {} 

     for j, c in enumerate(s):
         if c in occur and i <= occur[c]:
             ans = max(ans, j-i)
             i = occur[c] + 1  
             #directly skip to the next window to avoid the while loop in the first method
         occur[c]=j

     return max(ans, j-i+1)
