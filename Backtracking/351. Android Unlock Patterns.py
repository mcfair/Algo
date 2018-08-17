class Solution(object):
    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        jump = collections.defaultdict(int)
        for i in (1,4,7):
            jump[i,i+2]=jump[i+2,i] = i+1
        for j in (1,2,3):
            jump[j,j+6]=jump[j+6,j] = j+3
        jump[1,9]=jump[9,1]=jump[3,7]=jump[7,3]=5
        
        def backtrack(cur, remain):
            if remain==0:
                return 1
        
            count = 0
            visited[cur] = True
            for nxt in range(1,10):
                if not visited[nxt] and (not jump[cur,nxt] or visited[jump[cur,nxt]]):
                    count += backtrack(nxt, remain-1)
            visited[cur] = False
            
            return count
        
        visited = [0]*10    
        res = 0
        for k in range(m,n+1):
            res += backtrack(1, k-1)*4
            res += backtrack(2, k-1)*4
            res += backtrack(5, k-1)
        return res
