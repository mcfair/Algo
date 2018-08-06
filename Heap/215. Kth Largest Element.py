#heapify takes O(n)
#heappop takes O(logn)
#so total it takes O(klogn), k is guarenteed < n/2
#better than sort solution which takes O(nlogn): first sort then return nums[n-k]

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums) 
        
        if k > n:
            return None
        
        #use min heap  
        elif n/2 < k <= n:
            #print "use min heap"
            heapq.heapify(nums)
            for i in range(len(nums)-k ):
                heapq.heappop(nums)
            return  heapq.heappop(nums)
        #use max heap
        elif 0<= k <= n/2:
            #print "use max heap"
            nums = map(lambda x: -x, nums)
            heapq.heapify(nums)
            for i in range(k-1):
                heapq.heappop(nums)            
                
            return - heapq.heappop(nums)
        
        
