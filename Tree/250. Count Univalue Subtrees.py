
class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """ 
        
        def dfs(node, parentval):
            if not node: return True
            
            left = dfs(node.left, node.val)
            right = dfs(node.right, node.val)
            
            if left and right:
                self.ans += 1
                
            return left and right and node.val == parentval
        
        self.ans = 0
        dfs(root, None)
        return self.ans
