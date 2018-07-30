# it's basically to find all combinations
# to do that,we need a dynamically updated list
# similar to BFS code
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

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
