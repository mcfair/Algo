#O(nlogn) Binary Search
"""
tails array stores the smallest tail (last element) of all increasing subsequences with length i+1 in tails[i].
Traverse through nums array to update tails
This method can't be used to do backtracking.
"""
import bisect
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tails = [0]*len(nums)
        maxl = 0
        for num in nums:
            i = bisect.bisect_left(tails, num, 0, l)
            tails[i] = num
            if i == maxl:
                maxl+=1
        return maxl
