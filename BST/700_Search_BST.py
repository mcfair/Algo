#Very basic dfs, a building block for other BST problems
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return None
        if val == root.val:
            return root
        elif val < root.val:
            return self.searchBST(root.left, val)
        elif val > root.val:
            return self.searchBST(root.right, val)
