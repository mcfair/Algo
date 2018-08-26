#brutal force - geneate all abbrs - TLE
class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """        
        return abbr in self.genAbbr(word)
    
    def genAbbr(self, word):
        def dfs(pos, count, abbr):
            if pos==len(word):
                ans.append(abbr+str(count) if count>0 else abbr)
                return
            dfs(pos+1, count+1, abbr)
            dfs(pos+1, 0, abbr+str(count)+word[pos] if count>0 else abbr+word[pos])
        
        ans = []
        dfs(0,0,'')
        return ans

#iterative
class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """

        i = j = 0
        m, n = len(word), len(abbr)
        
        while i < m and j < n:
            if word[i] == abbr[j]:
                i, j = i+1, j+1
            elif abbr[j] == "0":
                return False
            elif abbr[j].isnumeric():
                k = j
                while k < n and abbr[k].isnumeric():
                    k += 1
                i += int(abbr[j:k])
                j = k
            else:
                return False
        return i == m and j == n
