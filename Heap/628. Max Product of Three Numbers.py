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
        
#heap
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
            
#manually find 5 variables
class Solution(object):
    def maximumProduct(self, nums):
        min1, min2 = float('inf'), float('inf')
        max1, max2, max3 = float('-inf'), float('-inf'), float('-inf')
        for num in nums:
            if min2 < num < max3:
                continue
            if num < min1:
                min1, min2 = num, min1
            elif num < min2:
                min2 = num
            if num > max1:
                max1, max2, max3 = num, max1, max2
            elif num > max2:
                max2, max3 = num, max2
            elif num > max3:
                max3 = num
                
        p1 = min1*min2*max1
        p2 = max1*max2*max3
        return max(p1,p2)
