class Solution(object):
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """  
        if len(words1)!=len(words2):
            return False
        
        self.papa = {}
        self.rank = {}
        
        for a, b in pairs:
            self.union(a,b)
        
        for w1,w2 in zip(words1, words2):
            if self.find(w1)!=self.find(w2):
                return False
        return True
    
    def find(self, x):
        if x not in self.papa:
            self.papa[x]=x
            self.rank[x]=0
            
        while x!=self.papa[x]:
            x, self.papa[x] = self.papa[x], self.papa[self.papa[x]]
            
        return x
    
    def union(self,x,y):
        x, y = self.find(x), self.find(y)
        if x!=y:
            if self.rank[x] < self.rank[y]:
                self.papa[x] = y
            elif self.rank[x] > self.rank[y]:
                self.papa[y] = x
            else:
                self.papa[y] = x
                self.rank[x] +=1
