class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        m, n = len(board), len(board[0])
        
        self.papa = {}
        self.rank = {}
        self.rank['Edge'] = 9999
        self.papa['Edge'] ='Edge'
        
        for i in range(m):
            for j in range(n):
                if board[i][j]=='O':
                    if i==0 or i==m-1 or j==0 or j==n-1:
                        self.papa[i,j] = 'Edge'
                        self.rank['Edge'] +=1
                    else:
                        self.papa[i,j] = (i,j)
                        self.rank[i,j] = 0
        
        for i in range(m):
            for j in range(n):
                if board[i][j]=='O':  
                    for nx, ny in ((i+1,j), (i-1,j),(i,j-1),(i,j+1)):
                        if 0<=nx<m and 0<=ny<n and board[nx][ny]=='O':
                            self.union((i,j),(nx,ny))
        for i in range(m):
            for j in range(n):
                if board[i][j]=='O':        
                    if self.find((i,j))!='Edge':
                        board[i][j] = 'X'
        
                    
    def find(self, x):
        while x!=self.papa[x]:
            x, self.papa[x] = self.papa[x], self.papa[self.papa[x]]
            
        return x
    
    def union(self,x,y):
        x, y = self.find(x), self.find(y)
        if x!=y:
            if self.rank[x] < self.rank[y]:
                self.papa[x] = y
            elif self.rank[x] > self.rank[y]:
                self.papa[y] = x
            else:
                self.papa[y] = x
                self.rank[x] +=1
           
