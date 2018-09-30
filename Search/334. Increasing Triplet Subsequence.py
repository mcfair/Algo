#O(n) to find an increasing triplet
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        l = m = float('inf')
        
        for r in nums:
            if m < r:
                return True
            elif r < l:
                l = r
            elif l < r < m:
                m = r
            #print l, m, r
        return False


#O(nlogk) Generalize to k element sub-array
#k is a constant, each search takes O(logk).  
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
        return k == 0
