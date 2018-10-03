"""
Similar to 124, path can go from child to parent or vice versa.
So the DFS function need to (1) update the longest path, (2) return the longest the left or right branch (not path)
path length := number of edges
"""
#verbose version
class Solution(object):
    def longestUnivaluePath(self, root):
        
        def dfs(root):
            if not root: return 0
       
            l=dfs(root.left )
            l=l+1 if root.left and root.left.val==root.val else 0

            r=dfs(root.right )
            r=r+1 if root.right and root.right.val==root.val else 0

            self.ans = max(self.ans,r+l)
            return max(l,r)
        
        self.ans = 0
        dfs(root)
        return self.ans
        
#compact version, but hard to read
class Solution(object):
    def longestUnivaluePath(self, root):
        
        def traverse(node, parent_val):
            if not node: return 0
            left = traverse(node.left, node.val)
            right= traverse(node.right, node.val)
            self.longest = max(self.longest, left + right)
            return 1 + max(left, right) if node.val == parent_val else 0
        
        self.longest = 0
        traverse(root, None)
        return self.longest      
        
        

        
        
