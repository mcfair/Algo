class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def inorder(root):
            if root:
                for x in inorder(root.left): yield x
                yield root
                for x in inorder(root.right): yield x
        
        prev = float('-inf')
        for x in inorder(root):
            if prev >= x.val:
                return False
            prev = x.val
        return True
        
