"""
O(nlogm+n) m is the unique numbers in nums        
"""
class Solution(object):
    def countSmaller(self, nums):
       
        #map unique numbers to its sorted rank: 1 ~ m
        #it basically maps an unbounded range to fixed size (easy for building BIT)
        #it is the same idea as quantization
        #FURTHER THOUGHT: how about "Larger Numbers After Self"? use reversed sorted rank
        rank = {v: i+1 for i, v in enumerate(sorted(set(nums)))}
        
        #build the BIT using rank not absolute value
        #Vanilla BIT is used for cumulative/prefix sum
        #Here we use it store the cumulative occurance 
        seen  = BinaryIndexedTree(len(rank)) 
        
        #O(nlogm)
        #traverse nums from right to left to compute "Smaller Numbers After Self"
        #FUTHER THOUGHT: how about "Smaller Numbers Before Self", traverse nums from left to right 
        ret = []
        for x in nums[::-1]:
            #how many elements smaller than x have been seen? 
            ret += seen.query(rank[x]-1),
            #increment the occurance of x 
            seen.increment(rank[x])
        return ret[::-1]
    
class BinaryIndexedTree(object):
    def __init__(self, n):
        self.sums = [0] * (n + 1)

    def increment(self, i, delta=1):
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
    
