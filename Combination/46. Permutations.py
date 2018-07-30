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
    
   
