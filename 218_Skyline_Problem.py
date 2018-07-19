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
		
		
