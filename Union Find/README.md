 class UnionFind(object):  
 
    def __init__(self):
        self.parent={}
        self.count =0
    
    def find(self,x):
        if x not in self.parent:
            self.parent[x] = x     
            self.count+=1
        
        ## no path compression
        #return x if x==self.parent[x] else self.find(self.parent[x])
        
        ## path compression
        while x!= self.parent[x]:
            x, self.parent[x] = self.parent[x], self.parent[self.parent[x]]
        return x
        
    def union(self,a,b):
        pa, pb = self.find(a), self.find(b)
        if pa!=pb:
            self.parent[pb] = pa
            self.count-=1
