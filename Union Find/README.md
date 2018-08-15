 class UnionFind(object):  
 
    def __init__(self):
        self.parent={}
        self.rank ={}
        self.count =0
    
    def find(self,x):
        if x not in self.parent:
            self.parent[x] = x     
            self.count+=1
            self.rank[x]=0
            
        ## no path compression
        #return x if x==self.parent[x] else self.find(self.parent[x])
        
        ## path compression
        while x!= self.parent[x]:
            x, self.parent[x] = self.parent[x], self.parent[self.parent[x]]
        return x
        
    def union(self,a,b):
        pa, pb = self.find(a), self.find(b)
        if pa!=pb:
            ## union by rank (next 3 lines), let high rank be low rank's parent
            if rank[pa] < rank[pb]:
                pa, pb = pb, pa
            self.rank[pa] += (self.rank[pa] == self.rank[pb])
                     
            self.parent[pb] = pa
            self.count-=1
