
class Solution(object):

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def find(i,j, word):
            if not word: 
                return True
            if not 0<=i<len(board) or not 0<=j<len(board[0]) or word[0]!=board[i][j]:
                return 
            tmp = board[i][j]
            board[i][j] ='#'
            ans = find(i+1,j, word[1:]) or find(i-1,j, word[1:]) or find(i,j+1, word[1:]) or find(i,j-1, word[1:])
            board[i][j] = tmp
            return ans
            
            
            
            
        if not word: return True
        
        for i, row in enumerate(board):
            for j, x in enumerate(row):
                if x==word[0]:
                    if find(i,j, word):
                        return True
        return False
        
        
