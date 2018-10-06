#Heap solution
def minmaxGasDist(self, s , K):

      d = (s[-1]-s[0])/float(K)
      heap = []
      
      for v1, v2 in zip(s, s[1:]):
          distance = float(v2-v1)
          count = max(1, int((v2-v1)/d))  
          K-= count-1
          heapq.heappush(heap, (-distance/count, distance, count))
      
      #K is decremented before the 2nd for loop
      for i in range(K):
          _, distance, count = heapq.heappop(heap)
          heapq.heappush(heap, (-distance/(count+1), distance, count+1))
      
      return -heap[0][0]
