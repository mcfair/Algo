"""
If no dual parenets:
    The problem reduces to LC684. Redundant Connection, just remove the last edge that forms the circle.


If there is dual parents:
	If there is no cycle, just return the second edge. 
    (Note that you still need to traverse the entire graph to make sure there is no circle, NO early return)

	If there is a cycle, due to nature of directed graph, only one of the dual edges is in the cycle.
		- If you find a cycle with first edge, remove the first edge.  
		- Otherwise, remove the second.
"""


class Solution(object):
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """ 
        n = len(edges) 
        self.parent = {}
        
        numParents = collections.defaultdict(int)           
        for p, q in edges: 
            numParents[q] += 1
       
        first, second = None, None #two edges pointing to the same node
        for p, q in edges:
            if numParents[q]> 1: #when q has two parents, find out the two edges
                if first:
                    second = (p,q) 
                    continue      #find the second edge, then skip union find
                else:
                    first = (p,q) #find the first edge then do the union find
                    
            if self.find(p) == self.find(q):  #when there is a circle
                return first or (p,q)
            
            self.union(p,q)
            
        return second
    
    def find(self, x): 
        if x not in self.parent:
            self.parent[x] = x
            
        while x!=self.parent[x]:
            x, self.parent[x] = self.parent[x], self.parent[self.parent[x]]
        return x
    
    def union(self, a,b):
        a, b = self.find(a), self.find(b)
        self.parent[b] = a
        
