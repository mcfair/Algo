# To handle duplication, just avoid inserting a number before any of its duplicates.
class Solution(object):
    def permuteUnique(nums):
            ret = [[]]
            for n in nums:
                temp = []
                for item in ret:
                    for i in xrange(len(item) + 1):
                        temp += item[:i] + [n] + item[i:],
                        if i < len(item) and item[i] == n:
                            break
                ret = temp
            
 class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
       
        ans = [[]]
        for x in nums:
            ans = [l[:i]+[x]+l[i:]
                   for l in ans
                   for i in xrange((l+[x]).index(x)+1)] #find the index of first x
        return ans
