class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        self.graph = graph
        self.ans = []
        self.findpath(0, [0])
        return self.ans
        
        
    def findpath(self, node, path):
        
        if node == len(self.graph)-1:
            self.ans.append(path)
            return
        for nxt in self.graph[node]:
            self.findpath(nxt, path+[nxt])
        return
            
     
