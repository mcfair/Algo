https://www.youtube.com/watch?v=2SVLYsq5W8M&t=1037s
    
#BIT aka Fenwick Tree
class BinaryIndexedTree(object):
    def __init__(self, n):
        self.sums = [0] * (n + 1)

    def update(self, i, delta):
        while i < len(self.sums):
            self.sums[i] += delta
            i += self._lowbit(i)

    def query(self, i):
        ret = 0
        while i > 0:
            ret += self.sums[i]
            i -= self._lowbit(i)
        return ret
    
    def _lowbit(self, i):
        return i & -i
    
class Solution(object):
    def countSmaller(self, nums):
        #O(mlogm+n) m is the unique numbers in nums
        #sort the unique numbers and map them to rank: 0 ~ m
        rank = {v: i for i, v in enumerate(sorted(set(nums)))}
        
        freq  = BinaryIndexedTree(len(rank)) 
        ret = [ ]
        
        #O(nlogm)
        #scan from right to left
        for x in nums[::-1]:
            ret += freq.query(rank[x]),
            freq.update(rank[x] + 1 , 1)
        return ret[::-1]
