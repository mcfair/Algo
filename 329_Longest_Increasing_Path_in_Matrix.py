#dp 200ms O(m*n)
#trick is to sort bu value and build dp from smaller values to larger values
class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        m,n = len(matrix), len(matrix[0])
        dp = collections.defaultdict(lambda:1)
        
        xyzarray = [ ]
        for i in range(m):
            for j in range(n):
                xyzarray.append((i,j,matrix[i][j]))
        xyzarray.sort(key=lambda x:x[2])
        
        ret=1
        for i,j, z in xyzarray:
                dp[i,j] = 1 + max(
                    dp[i-1,j] if i>0    and z>matrix[i-1][j] else 0,
                    dp[i+1,j] if i+1<m  and z>matrix[i+1][j] else 0,
                    dp[i,j-1] if j>0    and z>matrix[i][j-1] else 0,
                    dp[i,j+1] if j+1<n  and z>matrix[i][j+1] else 0,
                )
                ret = max(ret, dp[i,j])
        return ret

#DFS, without caching, it's O(2^(m+n))
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
