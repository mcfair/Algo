"""
774. Minimize Max Distance to Gas Station

Binary Search + Count

Binary Seach on  [0, max distance of the array)
Count step is to compute the number of new gas stations we can insert into the original array.

Explanation for "count+= math.ceil((st[i + 1] - st[i]) / mid) - 1"
Each "mid" is the guess to the min max distance between any two stations, 
the "count" represents how many more stations can we add to the array.
We can compute this count by trying to insert new stations between the 2 adjacent houses.
For any 2 adjacent houses, we divide their original distance by the min distance (mid), 
the division - 1 represents as many houses as we can into any 2 adjacent houses.

Why "left = mid", instead "left = mid +1"?
The type of left and right is double, the difference between them may be less than 1.

if count > K, it means mid is too small to realize using only K more stations.
if count <= K, it means mid is possible and we can continue to find a bigger one.
When left + 1e-6 >= right, it means the answer within 10^-6 of the true value and it will be accepted.

Time complexity:
O(NlogM), where N is station length and M is st[N - 1] - st[0]

Note: Answers within 10^-6 of the true value will be accepted as correct.
"""
#My implementaion
def minmaxGasDist(self, st , K):
        left, right = 1e-6, st[-1] - st[0]

        while left + 1e-6 < right:
            mid = (left + right) / 2
            count = 0
            for a, b in zip(st, st[1:]):
                count += int((b-a)/mid) 
            if count > K:
                left = mid + 1e-6
            else:
                right = mid
        return left   #return right also works


#Original answer from leetcode post
def minmaxGasDist(self, st, K):
        left, right = 1e-6, st[-1] - st[0]
        while left + 1e-6 < right:
            mid = (left + right) / 2
            count = 0
            for a, b in zip(st, st[1:]):
                count += math.ceil((b - a) / mid) - 1
            if count > K:
                left = mid  
            else:
                right = mid
        return right

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
