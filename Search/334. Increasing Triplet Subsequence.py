#O(n)
class Solution(object):
    def increasingTriplet(self, nums, k=3):
        """
        :type nums: List[int]
        :rtype: bool
        """
        inc = [float('inf')] * (k - 1)
        for x in nums:
            i = bisect.bisect_left(inc, x)
            if i >= k - 1:
                return True
            inc[i] = x
            print inc
        return k == 0
