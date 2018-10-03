"""
Subtleties behind this brilliant algorithm:

Bit masking
Greedy search based on prefix
Variation of 2sum: see below for the analogy

The classic 2sum problem actually achieved the acceleration from O(N^2) to O(N) by utilizing hashset's O(1) lookup time.

In 2sum, we want to find two numbers so that a + b = sum, naive way is to generate all pairs, and test each pair. 
That takes time O(N^2). Instead, we only look at one number at each iteration, and try to find sum - a in the HashMap.

In this problem (the second part where we try to update ans): we want to find two prefixs out of the hashset, 
such that prefix1 ^ prefix2 = tmp, with tmp being the greedily updated ans. Similiary to 2sum, 
we only look at one prefix at each iteration, and try to find  cand ^ prefix in the hashset. 

Note that A ^ B = tmp is equivalent to A = tmp ^ B,  A ^ tmp = B.
"""
class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = mask = 0
        
        for i in range(32, -1, -1):
            mask |= 1<<i
            hashset_ = set()
            for num in nums:
                hashset_.add(num & mask)
            cand = ans | (1 << i)  
            # ans is the maximum we can get if we consider only the most significant i - 1 bits
            # cand the potential max value we can get when considering the most significant i bits. 
            for prefix in hashset_:
                if cand ^ prefix in hashset_:
                    ans = cand
                    break
        return ans
    
"""
StefanPochmann's hard-to-read code
"""
class Solution(object):
    def findMaximumXOR(self, nums):
    
        ans = 0
        for i in reversed(range(32)):
            ans <<= 1
            prefixes = set([x >> i for x in nums])
            
            if any(answer^1 ^ p in prefixes for p in prefixes):
                ans += 1

          # else: on the next iteration, a '0' bit will be added
          # to the LSB because of the left shift

        return ans


#Trie approach
#don't understand the max matching for loop
class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        def build_tree():
            trie = {}
            for num in nums:
                node = trie
                for i in range(30, -1, -1):
                    bit = (num >> i) & 1
                    if bit not in node:
                        node[bit] = {}
                    node = node[bit]
            return trie
        
        # buld trie tree
        res = 0
        trie = build_tree()
        # max matching
        for num in nums:
            node, temp = trie, 0
            for i in range(30, -1, -1):
                bit = (num >> i) & 1
                if 1^bit in node:
                    node = node[1^bit]
                    temp |= 1<<i
                else:
                    node = node[bit]
            res = max(res, temp)
        return res
