class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a, b = 0, 0 # the result to the problem
        
        #1-liner solution for Leetcode136 Single Number
        #here it returns the XOR result of two single numbers 
        mask = reduce(operator.xor, nums)
        
        #get the lowest set bit 
        #here we know that a, b are different at this bit
        mask = self.lowbit(mask) 
        
        #Now, nums can be partitioned into two groups according to their bits at location i.
        #the first group consists of all numbers whose bits at i is 0.
        #the second group consists of all numbers whose bits at i is 1.
        #even occurences in each group are cancelled (like in Leetcode136), only left out single number
        for num in nums:
            if mask & num:
                a ^= num
            else:
                b ^= num
        return [a, b]
    
    def lowbit(self,x):
        return x&-x
