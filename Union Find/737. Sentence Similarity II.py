class UnionFind(object):
    def __init__(self):
        self.parent = {}
    
    def find(self, w):
        if w not in self.parent:
            self.parent[w] = w
            
        ##no path compression   
        #return w if self.parent[w] == w else self.find(self.parent[w])
        
        ##path compression
        while self.parent[w]!=w:
            self.parent[w], w = self.parent[self.parent[w]], self.parent[w]
        return w
        
    def union(self, a,b):
        pa, pb = self.find(a), self.find(b)
        if pa!=pb:
            self.parent[pa]=pb
    
    
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
        
        uf = UnionFind()
        for a, b in pairs:
            uf.union(a,b)
        

        for i in xrange (len(words1)):
            a,b = uf.find(words1[i]), uf.find(words2[i])
            if a != b:
                return False
            
        return True
