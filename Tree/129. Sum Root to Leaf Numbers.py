 
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        def dfs(root, numstr):
            if not root:
                return
            if not root.left and not root.right:
                self.ans += int(numstr+str(root.val))
            if root.left:
                dfs(root.left, numstr+str(root.val))
            if root.right:
                dfs(root.right, numstr+str(root.val))
            
        
        dfs(root,'')
        return self.ans
        
