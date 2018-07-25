class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if not matrix or not matrix[0]:
            return
            
        m, n = len(matrix), len(matrix[0])
        self.cumsum2D = collections.defaultdict(int)
        for i in range(m):
            for j in range(n):
                self.cumsum2D[i,j] = matrix[i][j] + self.cumsum2D[i-1,j] + self.cumsum2D[i,j-1] - self.cumsum2D[i-1,j-1]
        
    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
   
        return self.cumsum2D[row2, col2] + self.cumsum2D[row1-1, col1-1] \
                - self.cumsum2D[row2, col1-1] - self.cumsum2D[row1-1, col2]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
