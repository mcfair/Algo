#Iterative
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

#Solution 1: Recursive, take any number as first -Stefan
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)<=1: return [nums]
        
        return [[x] + p
                for i, x in enumerate(nums)
                for p in self.permute(nums[:i] + nums[i+1:])]
    
#Solution 2: Recursive, insert first number anywhere -Stefan
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)<=1: return [nums]
        
        return [p[:i] + [nums[0]] + p[i:]
                for p in self.permute(nums[1:])
                for i in range(len(nums))]
    
#My naive DFS implementation, same logic as Solution 1
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #return [x for x in itertools.permutations(nums)]
        def dfs(picked):
            if len(picked)==len(nums):
                ans.append([nums[i] for i in picked])
            for i in range(len(nums)):
                if i not in picked:
                    dfs(picked+[i])
        
        if len(nums)<=1: return [nums]
        ans = []
        for i in range(len(nums)):
            dfs([i])
        return ans
    
   
