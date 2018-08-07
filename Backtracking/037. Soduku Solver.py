https://leetcode.com/problems/sudoku-solver/description/
    
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.solve()
        
    def solve(self):
        i, j = self.getUnfilledPos()
        
        if i==-1 and j==-1:
            return True # Sudoku solved
        
        for d in '123456789':
            if self.isValid(i,j, d):
                self.board[i][j]=d
                if self.solve():
                    return True
                else:
                    self.board[i][j]='.'
        
    
    def getUnfilledPos(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] =='.':
                    return i,j
        return -1, -1
    
    def isValid(self,i,j,d):
        #check row and col
        for k in range(9):
            if self.board[i][k]==d  or  self.board[k][j]==d :
                return False
        #check box
        for k in range(i-i%3,i-i%3+3):
            for l in range(j-j%3,j-j%3+3):
                if self.board[k][l]==d:
                    return False
        return True
