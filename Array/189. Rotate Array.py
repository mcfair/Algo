#classical 3-step reverse 
def rotate(self, nums, k):
    """
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    if k==0: return 
    n = len(nums)  
    k %=n
    nums[:n-k] = reversed(nums[:n-k])
    nums[n-k:] = reversed(nums[n-k:])
    nums.reverse()

# not a good one
# put the last k elements in correct position (ahead) and do the remaining n - k. Once finish swap, the n and k decrease.
def rotate(self, nums, k):
    if k==0: return 
    n = len(nums)  
    k = k%n
    j = 0
    while n > 0 and k%n!=0:
        for i in xrange(0, k):
            nums[j + i], nums[len(nums) - k + i] = nums[len(nums) - k + i], nums[j + i] # swap
            print nums
        n, j = n - k, j + k
        k = k % n
