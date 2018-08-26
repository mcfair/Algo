 ```
 class UnionFind(object):  
 
    def __init__(self):
        self.parent={}
        self.rank = collections.defaultdict(int)
        self.count =0
    
    def find(self,x):
        if x not in self.parent:
            self.parent[x] = x     
            self.count+=1
            #self.rank[x]=0 #use defaultdict
            
        ## no path compression
        #return x if x==self.parent[x] else self.find(self.parent[x])
        
        ## path compression
        while x!= self.parent[x]:
            x, self.parent[x] = self.parent[x], self.parent[self.parent[x]]
        return x
            
     def union(self, x,y): #union by rank, let high rank be low rank's parent
        x, y = self.find(x), self.find(y)
        if x!=y:
            if self.rank[x] > self.rank[y]:
                self.papa[y] = x
            elif self.rank[x] < self.rank[y]:
                self.papa[x] = y
            else:
                self.papa[y] = x
                self.rank[x] +=1               
            self.count-=1
```
