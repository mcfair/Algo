class Trie(object):
    def __init__(self):
        self.root = {}
        
    def insert(self, word):
        curr = self.root
        for c in word:
            curr = curr.setdefault(c, {})
        curr['#'] = True
 
    
    def isValidWord(self,word):
        curr = self.root
        for c in word:
            if c not in curr:
                return (False, False)
            curr = curr[c]
        if '#' in curr and curr['#']:
            curr['#'] =False
            return (True, True)
        return (True, False) #(isPrefix, isWord)
        
class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if not board or not board[0]:
            return []
        
        trie = Trie()
        for word in words:
            trie.insert(word)
            
        m , n = len(board), len(board[0])
        visited, ans =[], []
        
        def backtrack(i,j, prefix):
            if not 0<=i<m or not 0<=j<n or (i,j) in visited:
                return
            
            prefix +=  board[i][j]
            isPrefix, isWord = trie.isValidWord(prefix)
            if not isPrefix: 
                return
            
            if isWord:
                ans.append(prefix)
            
            visited.append((i,j))
            backtrack(i+1,j, prefix)
            backtrack(i-1,j, prefix)
            backtrack(i,j+1, prefix)
            backtrack(i,j-1, prefix)
            visited.pop()
            
        
        for i in range(m):
            for j in range(n):
                if board[i][j] in trie.root:
                    backtrack(i,j,'')
        return ans
        
