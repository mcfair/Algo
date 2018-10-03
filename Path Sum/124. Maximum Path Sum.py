"""
Since paths can go from children to parents or from parents to children, the path sum can be defined as:
path_sum = max(0, left_child_sum) + current_node_val + max(0, right_child_sum)  #exclude negative children
we use path_sum to update self.maxsum

One important thing is that: it's NOT useful to return the path sum in the DFS function,
instead, we need to return current_node_val + max(0, left_child_sum, right_child_sum)
that's because in next round recursion, we need the sum of a sub branch (from a node to its child, to its grandchild ...)
"""
class Solution(object):
    def maxPathSum(self, root):
        self.maxsum = float('-inf')
        self.dfs(root)
        return self.maxsum
    
    def dfs(self, root):
        if not root: return 0
        lsum = max(0, self.dfs(root.left))
        rsum = max(0, self.dfs(root.right))
        self.maxsum = max(self.maxsum, lsum+rsum+root.val)
        return root.val + max(lsum,rsum)
        
