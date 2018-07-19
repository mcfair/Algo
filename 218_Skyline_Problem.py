#Hard

class Solution(object):
    def getSkyline(self, buildings):
        p = sorted(x for L,R,H in buildings for x in ((L,-H,R),(R,0,0)))
        ret, heap = [], []
        for L, negH, R in p:
            while heap and L >= heap[0][1]:
                heapq.heappop(heap)
            heapq.heappush(heap, (negH, R))
            if not ret or ret[-1][1] != -heap[0][0]: 
                ret.append([L, -heap[0][0]])
        return ret
		
		
#O(n^2) TLE
class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        
        sweep line method (from huahua's video)
        check all points on the vertical line, from high to low
        if the highest is aleft endpoint: it's a key point
        elif check the 2nd highest
        """
        events = [ event for b in buildings 
                    for event in ( (b[0], -b[2],0),  (b[1],b[2],1))]
        events.sort(key=lambda v: v)
        #larger height goes earlier, when using negative height
        q = [0] #heapq 
        sky = [] #result
        for v in events:
            heapq.heapify(q)
          
            #enter the building
            if v[2] ==0:
                premax = q[0]
                heapq.heappush(q, v[1])
                if premax !=q[0]:
                    sky.append([v[0], -v[1]])
            #leave the building
            else:
                premax = q[0]
                q.remove(-v[1])
                heapq.heapify(q)
                if premax!=q[0]:
                    sky.append([v[0], -q[0]])
           
        return sky
