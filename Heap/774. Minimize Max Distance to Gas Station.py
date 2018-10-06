"""
Heap solution is more intuitive.
Continually insert a new station in between the two stations which are the greatest distance apart from each other. 

One of the trick in the following implementation is the use of "cutoff", which is the upperbound of the answer.
Assuming there was only 2 stations, adding K stations evenly inbetween, we have (s[-1]-s[0])/float(K+1).
 
If the current gap is much larger than cutoff, the first for loop will give an accurate starting point of count. 
For example, say K=10,000 and there are 2 stations at positions 0 and 10,001. Both K and gap are very big, 
we don't want to increment count 1 by 1, with cutoff heap initialization, we start with a much proper initial value of count.

Actually without this cutoff trick, it will be TLE. With this trick, we are going to beat Binary Seach + Count method.
160ms (Heap) vs. 300ms(Binary Search)
"""

def minmaxGasDist(self, s , K):

      cutoff = (s[-1]-s[0])/float(K+1)
      heap = []
      
      #heap initialization based on cutoff
      for v1, v2 in zip(s, s[1:]):
          gap = float(v2-v1)
          count = max(1, int(gap/cutoff))  
          K-= count-1
          heapq.heappush(heap, (-gap/count, gap, count))
      
      #K is decremented before the 2nd for loop
      for i in range(K):
          _, gap, count = heapq.heappop(heap)
          heapq.heappush(heap, (-gap/(count+1), gap, count+1))
      
      return -heap[0][0]
