class Solution(object): 
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if numCourses < 2 or len(prerequisites) < 2: return True
        
        #build directed graph
        self.g = collections.defaultdict(set)
        for pre, post in prerequisites:
            self.g[post].add(pre)
        
        #flag for dfs: 0 - not visited,  1 - visiting, 2 - visited
        self.flag = [0]*numCourses
        
        #if there is circles in graph, then can't finish classes (return False)
        for i in range(numCourses):
            if self.hasCircle(i): return False
            
        return True
    
    def hasCircle(self, v):
        #dfs to find a circle: reaching a "visiting" node means there is a circle, 
        if self.flag[v] ==1 : return True
        if self.flag[v] ==2 : return False
        if not self.g[v]: return False
        
        self.flag[v] = 1
        for u in self.g[v]: 
            if self.hasCircle(u): return True
        self.flag[v] = 2
        
        return False
        
