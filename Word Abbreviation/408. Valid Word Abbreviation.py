
#recursive
class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """   
        def check(i, j):
            if i==len(word) and j==len(abbr):
                return True
            if i==len(word) or j==len(abbr):
                return False
            if word[i]==abbr[j]:
                return check(i+1,j+1)
            if abbr[j] in '123456789':
                k = j+1
                while k<len(abbr) and abbr[k] in '0123456789':
                    k+=1
                num = int(abbr[j:k])
                return check(i+num, k)
            return False
                
        return check(0,0)
    
#iterative - two pointers
class Solution(object):
    def validWordAbbreviation(self, word, abbr):

        i = j = 0
        m, n = len(word), len(abbr)
        
        while i < m and j < n:
            if word[i] == abbr[j]:
                i, j = i+1, j+1 
            elif abbr[j] in '123456789':
                k = j
                while k < n and abbr[k].isnumeric():  # in '0123456789'
                    k += 1
                i += int(abbr[j:k])
                j = k
            else:
                return False
        return i == m and j == n
    
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
