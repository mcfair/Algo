#Subsets II (with duplicates)
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
      
        # Get the frequency counts of numbers in "nums".
        cnts = collections.Counter(nums)
        res = [[]]
        for num, cnt in cnts.items():
            tmp = res[:] 
            # If "val" doesn't have duplicates, i.e., "cnt = 1", then
            # the new subsets of the set including "val" is the union
            # of the old subsets without "val" and the old subsets plus "val".
            # 
            # If "val" has duplicates, i.e., "cnt > 1", then the new
            # subsets of the set including "val" is the union of the
            # subsets with "i" "val"s where "0 <= i <= cnt".
            for i in range(1, cnt + 1):
                res += [[num]*i + pre for pre in tmp]
        return res


#compare to Subsets I solution below
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
