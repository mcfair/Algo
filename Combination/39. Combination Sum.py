class Solution:
    def combinationSum(self, candidates, target):
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], res)
        return res

    def dfs(self, nums, target, index, path, res):
        if target < 0:
            return  # backtracking
        if target == 0:
            res.append(path)
            return 
        for i in xrange(index, len(nums)):
            self.dfs(nums, target-nums[i], i, path+[nums[i]], res)


class Solution:
    def combinationSum(self, nums, target):
        res = []
        nums.sort()
        def dfs(left, path, idx):
            if not left: 
                res.append(path[:])
            else:
                for i, val in enumerate(nums[idx:]):
                    if val > left: break
                    dfs(left - val, path + [val], idx + i)
        dfs(target, [], 0)
        return res
