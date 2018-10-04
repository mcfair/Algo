#Method(1) naive single binary search: average O(logn), worst case O(n)
def searchRange(self, nums, target):
      l, r = 0, len(nums)
      while l<r:
          mid = (l+r)/2
          if nums[mid]==target:
              p=q=mid
              while p>l and nums[p-1]==target:
                  p-=1
              while q<r-1 and nums[q+1]==target:
                  q+=1
              return [p,q]
          if nums[mid] < target:
              l = mid+1
          else:
              r = mid
      return [-1,-1]

#Method(2) we can use two binary search to find left boundary and right boundary respectively
def bisect_left(nums, target):
      l, r = 0, len(nums) -1
      while l < r:
          m = (l + r) / 2
          if nums[m] < target:
              l = m + 1
          else:
              r = m
      return l if nums[l] == target else -1

def bisect_right(nums, target): 
      l, r = 0, len(nums) -1
      while l < r:
          m = (l + r) / 2 + 1  # Make mid biased to the right
          if nums[m] > target:
              r = m - 1
          else:
              l = m
      return l if nums[l] == target else -1

def searchRange(self, nums, target):
        if not nums: return [-1, -1]
        return [bisect_left(nums, target), bisect_right(nums, target)]

#Method(3) actually we can use bisect_left only, don't have to be confused with the revised bisect_right
def bisect_left(nums, target):
      l, r = 0, len(nums)
      while l < r:
          m = (l + r) / 2
          if nums[m] < target:
              l = m + 1
          else:
              r = m
      return l  


def searchRange(self, nums, target):
        if not nums: return [-1, -1]
        lo = bisect_left(nums,target)
        return [lo, bisect_left(nums,target+1)-1] if target in nums[lo:lo+1] else [-1, -1]

#Method(4) use python libary
class Solution(object):
    def searchRange(self, nums, target):
        if not nums: 
            return [-1,-1]
        
        lo = bisect.bisect_left(nums, target)
        
        if target not in nums[lo:lo+1]: #use list slice to avoid out-of-range error
            return [-1,-1]
        
        return [lo, bisect.bisect_right(nums, target, lo=lo)-1]  
