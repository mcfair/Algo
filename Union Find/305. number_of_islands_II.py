#count the number of islands after each addLand operation
class Solution(object):
    def numIslands2(self, m, n, positions):

        self.papa = {}
        self.rank = {}
        self.count= 0
        
        ans = [] 
        for i, j in positions:
            self.find((i,j))
            #visited.add((i,j))  #use self.papa as visited tracker 
            for nx,ny in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                if (nx,ny) in self.papa:
                    self.union((i,j),(nx,ny))
            ans.append(self.count)
        return ans
    
    def find(self,x):
        if x not in self.papa:
            self.papa[x] = x
            self.rank[x] = 0
            self.count += 1
        while x!=self.papa[x]:
            x, self.papa[x] = self.papa[x], self.papa[self.papa[x]]
        return x
    
    def union(self,a,b):
        a, b = self.find(a), self.find(b)
        if a!=b:
            if self.rank[a] > self.rank[b]:
                self.papa[b] = a
            elif self.rank[a] < self.rank[b]:
                self.papa[a] = b
            else:
                self.papa[b] = a
                self.rank[a] +=1
            self.count -=1
            
  
 
