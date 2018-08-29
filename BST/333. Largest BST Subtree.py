SubTree = collections.namedtuple('SubTree', 'largest, n, min, max') 
class Solution(object):
    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans = self.dfs(root)
        return ans.largest
    
    def dfs(self, root):
        if not root:
            #min=inf, max=-inf to make line 18 "if" statement invalid
            return SubTree(0,0, float('inf'), float('-inf')) 
           
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        if left.max < root.val < right.min:
            n = left.n + 1 + right.n
        else:
            n = float('-inf')
        largest = max(left.largest, right.largest, n)
        
        return SubTree(largest, n, min(left.min, root.val), max(right.max, root.val))
