class NumArray(object):

    def __init__(self, nums):
        self.n = len(nums)
        self.bit = [0] * (self.n + 1)
        self.nums = nums

        for i in xrange(self.n):
            self.add(i + 1, nums[i])


    def add(self,j,delta):
        #add delta
        while j <= self.n:
            self.bit[j] += delta
            j += j & -j

    def cumsum(self,j):
        res = 0
        while j >0:
            res += self.bit[j]
            j -= j &-j
        return res
    

    def update(self, i, val):
        #update with absolute value
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        self.add(i + 1, val - self.nums[i])
        self.nums[i] = val

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        if not self.nums: return  0
        return self.cumsum(j+1) - self.cumsum(i)
    



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
