"""
O(nlogn) is trivial.
Since we only need to konw top3 and min2 number, we should be able to do O(n(log3+log2)) = O(n)
"""
class Solution(object):
    def maximumProduct(self, nums):
        nums.sort()
      
        p1 = nums[0]*nums[1]*nums[-1]
        p2 = nums[-3]*nums[-2]*nums[-1]
        return max(p1, p2)
        
class Solution(object):
    def maximumProduct(self, nums):
        top3, min2 = [], []
        for x in nums:
            heapq.heappush(top3, x)
            heapq.heappush(min2, -x)
            if len(top3) > 3:
                heapq.heappop(top3)
            if len(min2) > 2:
                heapq.heappop(min2)
        
        p1 = top3[0]*top3[1]*top3[2]
        p2 = min2[0]*min2[1]*max(top3)
        return max(p1,p2)
            
