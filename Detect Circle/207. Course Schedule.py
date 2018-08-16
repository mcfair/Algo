class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if not prerequisites: 
            return True
        
        g = collections.defaultdict(list)
        for nxt, pre in prerequisites:
            g[pre].append(nxt)
            #g[nxt].append[pre], both lines will work
        
        visited = [0]*numCourses
        
        def hasCircle(i):
            if visited[i]==1: return True
            if visited[i]==2: return
            
            visited[i]=1
            for j in g[i]:
                if hasCircle(j):
                    return True
            visited[i]=2
        
        for i in range(numCourses):
            if hasCircle(i):
                return False
        return True
