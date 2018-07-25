class NumMatrix(object):
    def __init__(self, matrix):
        if not matrix or not matrix[0]:
            return
        self.matrix = matrix
        self.m= len(matrix)
        self.n= len(matrix[0])
        self.bit= [[0]*(self.n+1) for _ in range(self.m+1)]

        for i in range(self.m):
            for j in range(self.n):
                self.add(i+1 ,j+1 ,matrix[i][j])
                #Fenwick Tree index starting from 1
                
    #add delta to the Fenwich Tree
    def add(self,i,j,delta):
        x, y =[], []

        while i<=self.m:
            x.append(i)
            i+= i&-i

        while j<=self.n:
            y.append(j)
            j+= j&-j

        for i in x:
            for j in y:
                self.bit[i][j] += delta
                
    #cum sum from (0,0) to (i,j)
    def cumsum(self,i,j):
        x, y =[], []

        while i>0:
            x.append(i)
            i-= i&-i

        while j>0:
            y.append(j)
            j-= j&-j

        return sum(self.bit[i][j] for i in x for j in y)
    
    #update with absolute value 
    def update(self, row, col, val):
        delta = val - self.matrix[row][col]
        self.matrix[row][col] = val
        self.add(row +1,col+1, delta)

    #area from top-left (row1, col1) to bottom-right (row2+1, col2+1)
    #need add 1 to row2, col2, because Fenwick tree index starts from 1.
    def sumRegion(self, row1, col1, row2, col2):
        row2, col2 = row2+1, col2+1
        return self.cumsum(row2,col2) + self.cumsum(row1,col1) \
             -self.cumsum(row1,col2) - self.cumsum(row2,col1)
    
    
 
