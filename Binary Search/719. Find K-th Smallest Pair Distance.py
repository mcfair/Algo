#Binary Search + Counting (another binary search)

class Solution(object):
    def smallestDistancePair(self, nums, k):
        nums.sort() 
        n = len(nums)
        #search on the diffrence space, not on nums
        lo, hi = 0, nums[-1] - nums[0]
        
        while lo<hi:
            mid = (lo+hi)//2
            
            count = 0
            for i in range(n):
                j = bisect.bisect_right(nums, nums[i]+mid)
                count += j-i-1
            
            if count < k:
                lo = mid+1
            else:
                hi = mid
        return lo
    
# TLE version, while loop is O(n), while bisect_right is O(logn)
def smallestDistancePair(self, nums, k):

    nums.sort() 
    n = len(nums)
    #search on the diffrence space, not on nums
    lo, hi = 0, nums[-1] - nums[0]

    while lo<hi:
        mid = (lo+hi)//2

        count = 0
        for i in range(n):
            j = i+1
            while j<n and nums[j]-nums[i]<= mid:
                j+=1
            count += j-i-1

        if count < k:
            lo = mid+1
        else:
            hi = mid

    return lo
