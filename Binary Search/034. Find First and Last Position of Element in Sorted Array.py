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
