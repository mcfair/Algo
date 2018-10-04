  
#O(log(mn))
class Solution(object):
    def searchMatrix(self, matrix, target):
        if not matrix or target is None:
            return False

        rows, cols = len(matrix), len(matrix[0])
        low, high = 0, rows * cols - 1
        
        while low <= high:
            mid = (low + high) / 2
            num = matrix[mid / cols][mid % cols]

            if num == target:
                return True
            elif num < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return False

#O(log(m) + log(n))
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
        r = 0
        while r<m:
            if target== matrix[r][n-1]:
                return True
            elif target > matrix[r][n-1]:
                r = r+1
            else:
                l, h = 0, n-2
                while l<h:
                    m = (l+h)/2
                    if target < matrix[r][m]:
                        h = m-1
                    elif target > matrix[r][m]:
                        l = m+1
                    else:
                        return True
                return target == matrix[r][l] or target == matrix[r][h]
        return False
