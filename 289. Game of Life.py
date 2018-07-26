#To solve it in place, we use 2 bits to store 2 states:
#[2nd bit, 1st bit] = [next state, current state]
#0- 00  dead (next) <- dead (current)
#1- 01  dead (next) <- live (current)  
#2- 10  live (next) <- dead (current)  
#3- 11  live (next) <- live (current) 

#To get the current state, simply do
#board[i][j] & 1 (get last bit)

#To get the next state, simply do
#board[i][j] >> 1 (get leading bit)

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        rows, cols = len(board), len(board[0])
        
        #update board to encorprate the information of future state 
        #by using bit representation 0, 1, 2, 3
        for i in xrange(0, rows):
            for j in xrange(0, cols):
                #count the sorounding lives
                lives = self.countLiveNeighbours(board, rows, cols, i, j)
                
                #live cell with fewer than two live neighbors dies
                if board[i][j] == 1 and 2 <= lives <= 3:
                    board[i][j] = 3 #bin('11')
                    
                #dead cell with exactly three live neighbors becomes a live cell
                if board[i][j] == 0 and lives == 3:
                    board[i][j] = 2 #bin('10')
                
                #don't have to handle other cases who already has leading 0 for future state 'dead'
        
        #update board to next state
        for i in xrange(0, rows):
            for j in xrange(0, cols):
                board[i][j] = self.getFutureState(board[i][j])

    
    def countLiveNeighbours(self, board, rows, cols, i, j):
        """count the live neighbours"""
        directions = [(-1,-1), (0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,1), (-1,0)]
        count = 0
        for d in directions:
            ni, nj = d[0] + i, d[1] + j
            if 0 <= ni < rows and 0 <= nj < cols:
                count += self.getCurrentState(board[ni][nj])
        return count
    
    def getCurrentState(self, x):
        """get the last bit"""
        return x & 1
    
    def getFutureState(self, x):
        """get the leading bit"""
        return x >>1
