
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        T=collections.defaultdict(bool)
        
        #empty matches empty
        T[-1,-1]= True
        #empty string match pattern, 
        #only thing need to consider is whether '*' cancels its prefix
        for j in range(len(p)):
            if p[j]=='*':
                T[-1,j] = T[-1,j-2]
        
        for i in range(len(s)):
            for j in range(len(p)):
                if p[j] in {s[i], '.'}:
                    T[i,j] = T[i-1,j-1]
                elif p[j]=='*':
                    # zero occurence * cancels its prefix
                    if T[i,j-2]:
                        T[i,j] = T[i,j-2]
                    # occurence is one or more
                    elif p[j-1] in {s[i], '.'}:
                        T[i,j] = T[i-1,j]
                
        return T[len(s)-1,len(p)-1]
                     
                    
