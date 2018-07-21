#Easy 
#Simply DFS

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        def dfs(node, isLeft):
            if not node: 
                return 0
            if isLeft and not node.left and not node.right :
                return node.val
            return dfs(node.left, 1) + dfs(node.right, 0)
                
        return  dfs(root.left, isLeft=True) + dfs(root.right,isLeft=False)
