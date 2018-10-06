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
        left = 1e-6
        right = st[-1] - st[0]  #Theoretical upperbound is (s[-1]-s[0])/float(K+1). See line 64.

        while left + 1e-6 < right:
            mid = (left + right) / 2
            count = 0
            for a, b in zip(st, st[1:]):
                count += int((b-a)/mid) 
            if count > K:
                left = mid + 1e-6
            else:
                right = mid
        return left   #"return right" also works


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
