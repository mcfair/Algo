class Solution(object):
    def minAbbreviation(self, target, dictionary):
        """
        :type target: str
        :type dictionary: List[str]
        :rtype: str
        """
        n = len(target)
        if n==0: return ''
        if not dictionary: return str(n)
        
        abbrs = set([])
        for word in dictionary:
            if len(word)== n:  #pruning, only words with the same length may have conflict abbr
                abbrs |= self.genAbbr(word)
        
        uniques = self.genAbbr(target) - abbrs
        return sorted(list(uniques),key=len)[0]
        
        
    def genAbbr(self,word):
        def dfs(pos, count, abbr):
            if pos==len(word):
                ans.append(abbr+str(count) if count>0 else abbr)
                return
            dfs(pos+1, count+1, abbr)
            dfs(pos+1, 0, abbr+str(count)+word[pos] if count>0 else abbr+word[pos] )
            
        ans = []
        dfs(0, 0, '')
        return set(ans)
        
        
  #save some space
  class Solution(object):
    def minAbbreviation(self, target, dictionary):
        """
        :type target: str
        :type dictionary: List[str]
        :rtype: str
        """
        n = len(target)
        if n==0: return ''
        if not dictionary: return str(n)
        
        self.abbrs = set([])
        for word in dictionary:
            if len(word)== n:  #pruning, only words with the same length may have conflict abbr
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
