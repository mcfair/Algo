class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        g = collections.defaultdict(list)
        for a,b in prerequisites:
            g[a].append(b)
            
        plan = []
        seen = [0]*numCourses
        
        def hasCircle(i):
            if seen[i] ==1: return True
            if seen[i] ==2: return False
            seen[i]=1
            for j in g[i]:
                if hasCircle(j):
                    return True
            seen[i]=2
            
            #this is the only extra line, compared to 207.CourseSchedule1
            plan.append(i)
            
        for i in range(numCourses):
            if hasCircle(i):
                return []
        return plan
