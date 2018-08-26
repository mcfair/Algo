class Solution(object):
    def minAbbreviation(self, target, dictionary):
        """
        :type target: str
        :type dictionary: List[str]
        :rtype: str
        """
        n = len(target)
        
        #pruning(1) only words with the same length may have conflict abbr 
        dictionary = [word for word in dictionary if len(word) == n ]
        if not dictionary: return str(n)
        
        #pruning(2) if words differ at all positions, then no common abbr except "len(target)"
        dictionary = [word for word in dictionary if any(map(operator.eq, word, target))]
        if not dictionary: return target if n==1 else target[0]+str(n-1)
        
        self.abbrs = set([])
        for word in dictionary:
            self.abbrs |= set(self.genAbbr(word))
            
        return sorted(self.genAbbr(target),key=len)[0]
         
        
    def genAbbr(self,word):
        def dfs(pos, count, abbr):
            if pos==len(word):
                if count>0:
                    abbr+=str(count) 
                if abbr not in self.abbrs:
                    ans.append(abbr)
                return
            dfs(pos+1, count+1, abbr)
            dfs(pos+1, 0, abbr+str(count)+word[pos] if count>0 else abbr+word[pos] )
            
        ans = []
        dfs(0, 0, '')
        return ans
