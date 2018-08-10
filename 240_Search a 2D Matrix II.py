#O(m+n) 
#matrix is sorted from left to right and from top to bottom
#use top-right corner as pivot

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        
        m, n = len(matrix), len(matrix[0])
        
        r , c = 0, n-1
        while r<m and c>=0:
            if target < matrix[r][c]:
                c = c-1
            elif target > matrix[r][c]:
                r = r+1
            else:
                return True
        return False
