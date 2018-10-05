"""
Binary Search + Count

The time complexity is O(n * log(n) * log(R)), where n is number of rows in matrix, R is the range of the matrix, upto 2^32.
In a way, this is an O(n * log(n)) time and O(1) space solution.
We do binary search in R space, not the matrix space.

Same method is applied to solve LC287.
"""
def kthSmallest(self, matrix, k):
    lo = matrix[0][0]
    hi = matrix[-1][-1]
    
    while lo<hi:
        mid = (lo+hi)//2
        if sum(bisect.bisect_right(row, mid) for row in matrix) < k:
            lo = mid+1
        else:
            hi = mid
    return lo
    
    
"""
Heap - more intuitive solution when seeing "kth" smallest or largest. Time complexity is O(k * log n).
Things to learn from the code below: record (i,j) location along with the value.
Same method is used to solve LC23. Merge k Sorted Lists.
"""
def kthSmallest(self, matrix, k):
        heap = [(row[0], i, 0) for i, row in enumerate(matrix)]
        heapq.heapify(heap)
        ret = 0
        for _ in range(k):
            ret, i, j = heapq.heappop(heap)
            if j+1 < len(matrix[0]):
                heapq.heappush(heap, (matrix[i][j+1], i, j+1))
        return ret
