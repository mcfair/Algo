class Solution(object):
    def maximalRectangle1(self, matrix):
        #idea is to use cumsum to calculate any rectangle starting from (i,j) top-left to (k,l) bottom-right
        #O(n^4) TLE
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        if m==n==1: return int(matrix[0][0])
        
        cumsum = collections.defaultdict(int)
        for i in range(m):
            for j in range(n):
                cumsum[i,j] = cumsum[i-1,j] + cumsum[i,j-1] - cumsum[i-1,j-1]  + int(matrix[i][j])
        #area bounded by top-left (i,j) and bottom-right (k,l) inclusive
        maxarea = 0      
        for i in range(m):
            for j in range(n):
                for k in range(i,m):
                    for l in range(j,n):
                        area = cumsum[k,l] + cumsum[i-1,j-1] - cumsum[k,j-1] - cumsum[i-1,l]                     
                        if area == (k-i+1)*(l-j+1):
                            maxarea = max(maxarea, area)
                
        return maxarea
        
