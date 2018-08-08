class Solution(object):
    def exist(self, board, word):
        #O(4^|word|)
        def dfs(i,j, k):
            if not 0<=i<m or not 0<=j<n or board[i][j]!= word[k] or (i,j) in visited:
                return False
            if k == len(word) -1 :
                return True
            visited.append((i,j))
            # use 'or' to pass 88%
            # use any(list) having TLE
            res=dfs(i-1,j, k+1) or \
                dfs(i+1,j, k+1) or \
                dfs(i,j-1, k+1) or \
                dfs(i,j+1, k+1)
            visited.pop()
            return res
            
        m,n = len(board), len(board[0])
        
        #O(m*n*4^|word|)
        for i in range(m):
            for j in range(n):
                visited = []
                if dfs(i,j, 0):
                    return True
        return False
    
    
    
class Solution(object):
    def exist(self, board, word):
 
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
        
        
