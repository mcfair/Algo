
#path_length = left + right
#recursion returns the maxdepth not path length
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
                
        def depth(p):
            if not p: return 0
            left = depth(p.left)
            right = depth(p.right)
            self.ans = max(self.ans, left+right)
            return 1 + max(left, right)
        
        self.ans = 0   
        depth(root)
        return self.ans
