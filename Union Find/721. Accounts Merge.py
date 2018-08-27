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
