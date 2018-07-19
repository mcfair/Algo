class Solution(Object):
 	def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
		#when a node is None, return 0
        #when a node has no child, its depth = 1
        #when a node has single child, the depth is determined by this single child
        #when a node has two children, take the min of the two.
		
        if not root: return 0
        if not root.left and not root.right: return 1
		return 1 + min(self.minDepth(child) for child in (root.left, root.right) if child)
        
		
		#more verbosely
        if not root: return 0
        if not root.left and not root.right: return 1
        if not root.left:
            return 1 + self.minDepth(root.right)
        if not root.right:
            return 1 + self.minDepth(root.left)
        
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
