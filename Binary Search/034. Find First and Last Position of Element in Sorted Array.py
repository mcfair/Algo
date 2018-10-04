#naive single binary search: average O(logn), worst case O(n)
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

#we can use two binary search to find left boundary and right boundary respectively
class Solution:
    def searchRange(self, nums, target):
        if not nums:
            return [-1, -1]

        def bisect_left(nums, target):
            l, r = 0, len(nums) -1
            while l < r:
                m = (l + r) // 2
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m
            return l if nums[l] == target else -1

        def bisect_right(nums, target):
            l, r = 0, len(nums) -1
            while l < r:
                m = (l + r) // 2 + 1
                if nums[m] > target:
                    r = m - 1
                else:
                    l = m
            return l if nums[l] == target else -1

        return [bisect_left(nums, target), bisect_right(nums, target)]
                
                
