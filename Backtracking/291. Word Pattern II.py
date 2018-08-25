#there are numerous ways to split the string, so backtracking is required to test all cases
class Solution(object):
    def wordPatternMatch(self, pattern, string):
        def backtrack(  i, j, ptable={}, stable={}):
            if i == len(pattern) and j == len(string): return True
            if i == len(pattern) or j == len(string): return False
            
            p = pattern[i]
            for k in range(j, len(string)): #try various word length for "s"
                s = string[j:k+1] 
                if p not in ptable and s not in stable:  # case (1) no mapping defined
                    ptable[p], stable[s]  = s, p
                    if backtrack( i+1, k+1, ptable, stable):
                        return True
                    del ptable[p]
                    del stable[s]
                    
                elif p in ptable and ptable[p] == s: # case(2) match the current mapping, check next
                    if backtrack( i+1, k+1, ptable, stable):
                        return True
                    
                else:             # case(3) do not match current mapping, then try another word length
                    continue
            return False          #tried everything but no luck

        return backtrack(i=0, j=0)
