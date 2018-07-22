class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if len(edges) != n-1:
            return False
        
        g = collections.defaultdict(list)
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
            
        seen = [0]*n
        
        def dfs(i):
            if seen[i]:
                return
            seen[i]=1
            for nei in g[i]:
                dfs(nei)
        
        dfs(0)
        return sum(seen)==n
            
