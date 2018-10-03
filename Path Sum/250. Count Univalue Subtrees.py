"""
LC250
uni-value subtree has all nodes with the same value. Each leaf is considered a uni-value subtree.
pass parent.val to the DFS function to compare 
"""
def countUnivalSubtrees(self, root):

    def dfs(node, parentval):
        if not node: return True
        left = dfs(node.left, node.val)
        right = dfs(node.right, node.val)

        if left and right:
            self.count += 1
        return left and right and node.val == parentval

    self.count = 0
    dfs(root, None)
    return self.count

"""
compare and contrast to LC687
pass parent.val to the DFS function
"""
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
        
