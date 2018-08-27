class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        self.papa = {}
        self.rank = {}
        email2name= {}
        
        for acc in accounts:      
            name = acc[0]
            for email in acc[1:]:
                email2name[email] = name
                self.union(email, acc[1])
        
        tree = collections.defaultdict(list)
        for email in email2name:
            tree[self.find(email)].append(email)
        
        ret = []
        for email in tree:
            ret.append([email2name[email]] + sorted(tree[email]))
            
        return ret
            
    def find(self, x): #with path compression
        if x not in self.papa:
            self.papa[x] = x
            self.rank[x] = 0
        while x!=self.papa[x]:
            x, self.papa[x] = self.papa[x], self.papa[self.papa[x]]
        return x
    
    def union(self,x,y): #union by rank
        x, y = self.find(x), self.find(y)
        if x!=y:
            if self.rank[x] > self.rank[y]:
                self.papa[y] = x
            elif self.rank[x] < self.rank[y]:
                self.papa[x] = y
            else:
                self.papa[x] = y
                self.rank[y] +=1

                
                
                
#DFS
class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        #Build Graph
        graph = collections.defaultdict(list)
        for i, acc in enumerate(accounts):
            name = acc[0]
            for email in acc[1:]: 
                graph[email].append(i)
        
        def dfs(i):
            if i in visited:
                return
            visited.add(i)
            for email in accounts[i][1:]: 
                emails.add(email)
                for j in graph[email]:
                    dfs(j)
        
        #Perform DFS         
        visited, res = set(), []
        for i, acc in enumerate(accounts):
            if i in visited:
                continue 
            emails = set()
            dfs(i)
            res.append([acc[0]] + sorted(emails))
        return res
