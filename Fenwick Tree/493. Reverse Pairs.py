#There are many ways to solve this problem: BST, BIT, Merge-Sort

class BIT(object):
    def __init__(self, n):
        self.n = n + 1
        self.sums = [0] * self.n
    
    def update(self, i, delta=1):
        while i < self.n:
            self.sums[i] += delta
            i += i & (-i)
    
    def query(self, i):
        res = 0
        while i > 0:
            res += self.sums[i]
            i -= i & (-i)
        return res

class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #include all 2*x and remove duplicates
        new_nums = set(nums + [x * 2 for x in nums])
        sorted_set = sorted(list(new_nums))
        
        
        ranks = {v:i for i, v in enumerate(sorted_set)}
             
        tree = BIT(len(sorted_set))
        #reverse order
        res = 0
        for x in nums[::-1]:
            res += tree.query(ranks[x])
            tree.update(ranks[x * 2]+1)
        return res
