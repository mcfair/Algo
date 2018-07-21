class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        if not root:
            return None
        if target == root.val:
            return root.val
        
        kid = root.left if target < root.val else root.right
        
        if not kid:
            return root.val
        
        kidval = self.closestValue(kid, target)
        
        if abs(root.val -target) <= abs(target -kidval):
            return root.val
        else:
            return kidval
    
