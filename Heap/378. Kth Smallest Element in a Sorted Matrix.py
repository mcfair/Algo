    
"""
Heap -  intuitively you would think of heap when being asked for "kth" smallest or largest. 
Time complexity is O(k * log n).
Use tuple in the heap to record i,j location along with the value.

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
