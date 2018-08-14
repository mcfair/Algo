class Trie:
    def __init__(self):
        self.root = {}
    
    def insert(self, word):
        curr = self.root
        for c in word:
            curr = curr.setdefault(c, {})
        curr['#'] = word
        
    def prefix(self, word):
        curr = self.root
        for c in word:
            if c not in curr:
                return False
            curr = curr[c]
        return True
    
    def search(self, word):
        curr = self.root
        for c in word:
            if c not in curr:
                return False
            curr = curr[c]
        return '#' in curr
    
class Solution:
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        trie = Trie()
      
        for word in words:
            trie.insert(word)
        m,n = len(board), len(board[0])
        
        ans, visited = [],[]
        
        def check(i,j, x):
            if not 0<=i<m or not 0<=j<n or (i,j) in visited:
                return 
            if not trie.prefix(x+board[i][j]):
                return
            
            x +=  board[i][j]
            if trie.search(x) and x not in ans:
                ans.append(x)
                    
            visited.append((i,j))
            check(i-1,j, x)
            check(i+1,j, x )
            check(i,j-1, x)
            check(i,j+1, x )
            visited.pop()
            
            
        for i, row in enumerate(board):
            for j, c in enumerate(row):
                if trie.prefix(c):
                    check(i,j, '')
        return ans
