"""
When pivot has duplicates, nums[0]==nums[-1], the solution for LC33 doesn't apply here anymore
"""
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums: return False
        if target == nums[0]: return True
        
        pivot = nums[0]
        l, r = 0, len(nums)
        while r>1 and nums[r-1] == pivot:
            r-=1
        
        while l<r:
            mid = (l+r)//2
            compare = nums[mid]
            if (target < pivot) ^ (compare < pivot):
                if target < pivot:
                    compare = float('-inf')
                else:
                    compare = float('inf')
            if compare == target: 
                return True
            if compare < target:
                l = mid + 1
            else:
                r = mid
        return False
