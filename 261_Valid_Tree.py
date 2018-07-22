#DFS
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
   
#Union-Find
class Solution(object):
    def validTree(self, n, edges):

        if len(edges)!=n-1:
            return False
        
        self.papa = range(n)
        self.count = n
        map(self.union, edges)
        
        return self.count==1

    def union(self, (a,b)):
        pa, pb = self.find(a), self.find(b)
        if pa != pb:
            self.papa[pa] = pb
            self.count -=1
        
    def find(self, x):
        if x != self.papa[x]:
            self.papa[x] = self.find(self.papa[x])
        return self.papa[x]
         
#Stefen Union-Find
class Solution(object): 
  def validTree(self, n, edges):
    parent = range(n)
    def find(x):
        return x if parent[x] == x else find(parent[x])
    def union(xy):
        x, y = map(find, xy)
        parent[x] = y
        return x != y
    return len(edges) == n-1 and all(map(union, edges))
