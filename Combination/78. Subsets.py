# Subsets I (no duplicates)        
# it's basically to find all combinations
# to do that,we need a dynamically updated list
# similar to BFS code
class Solution(object):
    def subsets(self, nums):

        result = [[]]
        for num in nums:
            result +=[[num] + pre for pre in result]
        return result
                      
        """
        print [[num] + pre for pre in result]
        [[1]]
        [[2], [2, 1]]
        [[3], [3, 1], [3, 2], [3, 2, 1]]
        """

#compare and contrast with solution to Leetcode 46 Permutations
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = [[]]
        for x in nums:
            ans = [l[:i]+[x]+l[i:]
                   for l in ans
                   for i in xrange(len(l)+1)]
        return ans
