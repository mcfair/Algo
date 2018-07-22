class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        m,n = len(matrix), len(matrix[0])
        
        directions = [(0,1),(0,-1), (-1,0), (1,0)]
        cache = { }
        
        def isSmaller(i,j,k,l):
            if  0<=k<m and 0<=l<n:
                return matrix[i][j] > matrix[k][l]
            return False
        
        def dfs(i,j, depth):
            if (i,j) in cache:
                return cache[i,j] +depth-1
            
            ret = [depth]
            for dx,dy in directions:
                if isSmaller(i,j,i+dx,j+dy):
                    ret.append(dfs(i+dx,j+dy,depth+1))
            return max(ret)
        res = []
        for i in range(m): 
            for j in range(n):
                    tmp = dfs(i,j,1) 
                    cache[i,j] =tmp
                    res.append(tmp)
        return max(res)
