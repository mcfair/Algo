class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.bit = [0]*(len(nums)+1)
        for i,x in enumerate(nums):
            self._add(i+1, x)
        
    def _add(self, i, delta):
        while i<len(self.bit):
            self.bit[i]+=delta
            i += (i&-i)
        
    def _query(self, i):
        cumsum = 0
        while i>0:
            cumsum += self.bit[i]
            i -= (i&-i)
        return cumsum
        
    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        delta = val - self.nums[i] 
        self._add(i+1, delta)
        self.nums[i] = val
        
    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self._query(j+1) - self._query(i)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
