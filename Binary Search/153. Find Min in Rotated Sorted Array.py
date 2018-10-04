 class Solution(object):
    def findMin(self, nums):
        
        #this if statement handles two cases: 
        #1. when len(nums)==1, nums[0] = nums[-1]
        #2. when nums is not rotated, nums[0] < nums[-1] 
        if nums[0] <= nums[-1]: 
            return nums[0]
        
        l, r = 0, len(nums)
        while l<r:
            mid = (l+r)//2
            if nums[mid-1] > nums[mid]:
                return nums[mid]
            if nums[mid] > nums[0]: #mid is in the left half
                l = mid+1
            else:
                r = mid
       
