"""
A backtracking problem
"""
class Trie(object):
    def __init__(self):
        self.trie = {}
    
    def insert(self, word):
        curr = self.trie
        for w in word:
            curr = curr.setdefault(w,{})
        curr['#'] = word
        
    def isWord(self, word):
        curr = self.trie
        for w in word:
            if w not in curr:
                return False
            curr = curr[w]
        return '#' in curr
        
        
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """                 

        if not s or not wordDict:
            return []
        
        self.trie=Trie()
        for word in wordDict:
            self.trie.insert(word)
       
        self.memo = collections.defaultdict(list)
         
        return self.dfs(s)
      
    def dfs(self, s):
        if s in self.memo:
            return self.memo[s]

        ans = []

        if self.trie.isWord(s):
            ans.append(s)

        for j in range(len(s)):
            left, right = s[:j] , s[j:]

            if self.trie.isWord(right): 
                for left_ans in self.dfs(left):
                    ans.append(left_ans +' ' +right)

        self.memo[s] = ans
        return ans
