 

def arrayPairSum(self, nums):
    return sum(sorted(nums)[::2])

"""
Since we know all the integers in the array will be in the range of [-10000, 10000],
we can do counting sort
"""
def arrayPairSum(self, nums):
 
      cnt = [0]*20001
      for x in nums:
          cnt[x+10000] += 1
      
      ans, odd = 0, False
      for idx, freq in enumerate(cnt):
          if freq:
              freq = freq-1 if odd else freq
              if freq&1:
                  ans += ((freq//2) + 1)*(idx-10000)
                  odd = True
              else:
                  ans += (freq//2)*(idx-10000)
                  odd = False
      return ans
  
