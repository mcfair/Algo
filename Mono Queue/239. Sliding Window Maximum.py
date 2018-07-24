class Monoqueue:
    def __init__(self):
        self.dqueue = []

    def push(self, val):
        count = 0
        while len(self.dqueue) > 0 and self.dqueue[-1][0] < val:
            count += self.dqueue[-1][1] + 1
            self.dqueue.pop()
        self.dqueue.append([val, count])   

    def getMax(self):
        return self.dqueue[0][0]

    def pop(self):
        if self.dqueue[0][1] > 0:
            self.dqueue[0][1] -= 1
            return
        self.dqueue.pop(0)
        
        
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        if len(nums) < 1:
            return []

        retval = []
        mq = Monoqueue()

        k = min(k, len(nums))

        for ii in range(k-1):
            mq.push(nums[ii])

        for ii in range(k-1 , len(nums)):
            mq.push(nums[ii])
            retval.append(mq.getMax())
            mq.pop()
        return retval
