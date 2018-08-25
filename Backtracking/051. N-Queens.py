#fill row by row
#for each row, check col by col "isvalid"
#diagonal 45degree can be represented by x+y = const
#diagonal 135degree can be represented by x-y = const

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """ 
        def dfs(r):
            if r == n:
                res.append([ '.'*c +'Q'+'.'*(n-c-1) for c in b])
                return
            
            for c in xrange(n):  #check col by col
                if isValid(r, c):
                    b[r]=c
                    dfs(r + 1)      # fill next row
                    b[r]=-1
        
        def isValid(r, c): #check whether we can place a Queen at posistion (r,c)
            for i, j in enumerate(b[:r]):#only need to check first r-1 row
                if c == j or i+j == r+c or i-j == r-c:     
                    return False
            return True
                        
        
        b = [-1]*n  #col id in each row: (r, b[r]) represents the position of Q
        
        res = []
        dfs(0)      # start from row 0
        return res
