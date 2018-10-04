def search(self, nums, target):
    if not nums: return -1

    l, r = 0, len(nums) 
    pivot = nums[0]

    while l <  r:
        mid = (l+r)//2
        if (target< pivot) == (nums[mid]<pivot): #target and nums[mid] in the same zone
            comparator = nums[mid]
        else:
            if target < pivot: 
                comparator = float('-inf')
            else:
                comparator = float('inf')
        #regular binary search
        if target == comparator: 
            return mid
        if target > comparator:
            l = mid+1
        else:
            r = mid
    return -1
