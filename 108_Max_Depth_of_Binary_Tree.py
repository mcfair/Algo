class Solution(object):
	def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
		#dfs
		if not root: return 0
		return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
		
		
		#bfs
		row, depth = [root], 0
		while any(row):
			row = [child for x in row
							for child in (x.left, x.right) if child]
			depth +=1
		return depth
