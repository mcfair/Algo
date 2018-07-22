# 44ms 
# If m operations (here m edges), either Union or Find, are applied to n elements, 
# the total run time is O(m log*n), where log* is the iterated logarithm. ~=O(4m)= O(m)
class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        self.papa = [i for i in range(n)]
        self.count = n
        for a, b in edges:
            self.union(a,b)
            
        return self.count
    
    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a!=b:
            self.papa[a] = b
            self.count -=1
    
    def find(self, a):
        if a != self.papa[a]:
            self.papa[a] = self.find(self.papa[a])
        return self.papa[a]
        
#use dict to save space for sparse graph   
class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        
        self.papa = {}
        self.count = n
        for a, b in edges:
            self.union(a,b)
            
        return self.count
    
    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a!=b:
            self.papa[a] = b
            self.count -=1
    
    def find(self, a):
        if a != self.papa.setdefault(a,a):
            self.papa[a] = self.find(self.papa[a])
        return self.papa[a]

# DFS O(m+n)
class Solution(object):
    def countComponents(self, n, edges):
 
        #construct graph
        g = collections.defaultdict(list)
        for u, v in edges:
            g[v].append(u)
            g[u].append(v)
            
        visited, count = set(), 0
        
        #standar DFS
        def dfs(i):
            if i in visited:
                return
            visited.add(i)
            for x in g[i]:
                dfs(x)
        
        for i in range(n):
            if i not in visited:
                count +=1
                dfs(i)
        
        return count

#BFS
class Solution(object):
    def countComponents(self, n, edges):
  
        #construct graph
        g = collections.defaultdict(list)
        for u, v in edges:
            g[v].append(u)
            g[u].append(v)
            
 
        visited, count = set(), 0
        
        def bfs(node):
            queue = [node]
            for n in queue:
                for nei in g[n]:
                    if nei not in visited:
                        visited.add(nei)
                        queue.append(nei)
        
        for i in range(n):
            if i not in visited:
                count += 1
                bfs(i)
                
        return count
