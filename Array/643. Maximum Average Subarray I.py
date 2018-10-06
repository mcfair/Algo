
#two pointers
def findMaxAverage(self, nums, k):
    windowsum = sum(nums[:k])
    maxsofar = windowsum
    l, r = 0, k
    while r < len(nums):
        windowsum += nums[r] - nums[l]

        maxsofar = max(maxsofar,  windowsum)
        l, r = l+1, r+1

    return maxsofar/float(k)
    
#one pointer
#This is a fixed size window, why do we need two pointer....

def findMaxAverage(self, nums, k):
    maxn = sum(nums[:k])
    temp = maxn
    for i in range(len(nums) - k):
        temp = temp - nums[i] + nums[i + k]
        maxn = max(maxn, temp)
    return maxn / float(k)
