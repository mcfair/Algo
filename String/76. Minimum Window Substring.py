class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """ 
        missing = len(t)                         #total number of chars need to find
        needed = collections.defaultdict(int)    #hash table to store char frequency
        for c in t: 
            needed[c] += 1
     
        start, end = 0, 0                        #(start, end) pointers to store min window
        i = 0                                    #(i,j) is the moving window
        for j, char in enumerate(s, 1):          #index j from 1, move j to find matches
            if needed[char] > 0:
                missing -= 1
            needed[char] -= 1                    #needed can be negative, which represents  
                                                 #either redundant char in t
                                                 #or char in set(s)-set(t)
                    
            if missing == 0:                     #all chars matched, let's move i now.
                while i<j and needed[s[i]] < 0:  #remove redundent chars to find the true i 
                    needed[s[i]] += 1
                    i += 1
                    
                if end == 0 or j-i < end-start:  #update window
                    start, end = i, j
                
                needed[s[i]] += 1                #update needed and missing before moving i to i+1
                missing += 1  
                i += 1
                
        return s[start:end]
