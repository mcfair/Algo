#Easy
#O(1) range sum is the building block for many other problems

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.cumsum = collections.defaultdict(int)
        for i, x in enumerate(nums):
            self.cumsum[i] = self.cumsum[i-1] + x

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        #O(1)
        return self.cumsum[j] -self.cumsum[i-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
