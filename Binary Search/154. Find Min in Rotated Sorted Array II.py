class Solution(object):
    def findMin(self, nums):

        pivot = nums[0]
        l, r = 0, len(nums)
        
        while r>0 and nums[r-1]==pivot:
            r-=1
        while l<r and nums[l+1]==pivot:
            l+=1
        #till this point, only one unique pivot should stay inside [l, r)    
        
        #handles two cases: only one element left or [l,r) is sorted
        if l==r or nums[l] < nums[r-1]: 
            return pivot
        
        #regular binary search
        while l<r:
            mid = (l+r)//2
            if nums[mid-1] > nums[mid]:
                return nums[mid]
            if nums[mid] > nums[0]: #mid is in the left half
                l = mid+1
            else:
                r = mid
