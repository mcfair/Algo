#don't understand yet
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
