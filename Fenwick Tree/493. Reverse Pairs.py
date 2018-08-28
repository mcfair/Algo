#There are many ways to solve this problem: BST, BIT, Merge-Sort

class BIT(object):
    def __init__(self, n):
        self.n = n + 1
        self.sums = [0] * self.n
    
    def update(self, i, delta):
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
        tree = BIT(len(sorted_set))
        res = 0
        ranks = {}
        for i, n in enumerate(sorted_set):
            ranks[n] = i + 1

        #reverse order
        for x in nums[::-1]:
            res += tree.query(ranks[x] - 1)
            tree.update(ranks[x * 2], 1)

        return res
