class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        def dfs(r):
            if r ==n:
                self.count +=1
                return
            for c in range(n):
                if isvalid(r,c):
                    b[r] = c 
                    dfs(r+1)
                    b[r] = -1
                    
        def isvalid(r,c):
            for i,j in enumerate(b[:r]):
                if c==j or i+j==r+c or i-j==r-c:
                    return False
            return True
                
        
        b = [-1]*n
        self.count = 0
        dfs(0)
        return self.count
        
