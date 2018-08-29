 class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = float('-inf')
        self.dfs(root)
        return self.res
    
    def dfs(self, root):
        if not root: return 0
        left = max(0, self.dfs(root.left))
        right = max(0, self.dfs(root.right))
        self.res = max(self.res, left+right+root.val)
        return root.val + max(left,right)
        
