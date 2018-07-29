#Naive solution is to just count the array, and find the single number. O(n) time with extra space O(k)

#Solution based on bit manupilation is O(1) space.
#Logic: XOR will return 1 only on two different bits. So if two numbers are the same, XOR will return 0. 
#A ^ A = 0 and A ^ B ^ A = B.  Finally only one number left. 
#This only works for even number of A, so it doesn't solve Leetcode137. Single Number II

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """  
        return reduce(lambda x, y: x ^ y, nums)
