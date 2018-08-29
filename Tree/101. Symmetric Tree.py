class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        
        def isSym(l, r):
            if not l and not r:
                return True
            if not l or not r:
                return False
            if l.val!=r.val:
                return False
            return isSym(l.left, r.right) and isSym(l.right, r.left)
            
        return isSym(root.left, root.right)
