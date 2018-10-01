
def minWindow(s, t):
    needed = collections.Counter(t)          #hash table to store char frequency
    missing = len(t)                         #total number of chars we need to find
    start, end = 0, 0                        #(start, end) pointers to store min window
    i = 0                                    #(i,j) is the moving window
    for j, char in enumerate(s, 1):          #index j from 1, move j to find matches
        if needed[char] > 0:
            missing -= 1
        needed[char] -= 1                    #needed can be negative, which represents redundency (more than needed)
        
        if missing == 0:                     #all chars matched, let's move i now.
            while i < j and needed[s[i]] < 0:  #remove redundent chars to find the i to form the min window
                needed[s[i]] += 1
                i += 1
            needed[s[i]] += 1                #make sure the first appearing char satisfies need[char]>0
            missing += 1                     #we missed this first char, so add missing by 1
            if end == 0 or j-i < end-start:  #update window
                start, end = i, j
            i += 1                           #update i to start+1 for next window
    return s[start:end]
