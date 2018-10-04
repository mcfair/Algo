"""
The difficulty in this problem lies in O(1) space, and many solution using O(n) space can also be accepted by OJ.
The solution is applying bi-search in the range[1, n] by counting the element which falls in sub range(n/2, n].
If the number is bigger than capacity of that sub range, it means the duplicated integer falls in the sub-range.
Otherwise the duplicated integer falls in the other half sub range.

This is binary search on (0,N] domain, not binary search on nums.  We count nums inside binary search. 
So the time is O(nlogn)
"""

class Solution(object):
    def findDuplicate(self, nums):
   
        low, high = 0, len(nums)-1
       
        while high - low >1:
            mid = (high + low) / 2
            count = sum(mid< i<=high for i in nums)   #count of elements inside (mid,high]
      
            if count > high - mid: #if count is more than the range span, we know duplicates is inside this range.
                low = mid
            else:
                high = mid
       
        return high
