#There are many ways to solve this problem: BST, BIT, Merge-Sort

#Code is almost identical to 315. Count of Smaller Numbers After Self

class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #include all 2*x and remove duplicates
        new_nums = list(set(nums + [2*x for x in nums]))
        
        #quantization
        rank = {v: i+1  for i,v in enumerate(sorted(new_nums))}
        
        #cumulative occurance table
        seen = BIT(len(rank))
        
        #reverse order traversal
        res = 0
        for x in nums[::-1]:
            #how many elements smaller than x have been seen?
            res += seen.query(rank[x] - 1)
            #increment the occurance of 2*x
            seen.increment(rank[2*x])

        return res
    
    
class BIT(object):
    def __init__(self, n):
        self.n = n + 1
        self.sums = [0] * self.n
    
    def increment(self, i, delta=1):
        while i < self.n:
            self.sums[i] += delta
            i += i & (-i)
    
    def query(self, i):
        res = 0
        while i > 0:
            res += self.sums[i]
            i -= i & (-i)
        return res
