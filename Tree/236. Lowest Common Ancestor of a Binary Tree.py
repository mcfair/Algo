#DFS
def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        #find p or q or None
        if root in (None, p, q): return root
        
        left = self.lowestCommonAncestor( root.left, p, q) 
        right = self.lowestCommonAncestor(root.right, p, q)
        
        #found p, q in different branches, then current node (root) is the LCA
        if left and right:
            return root
        #otherwise, it must be the one that is NOT NONE.
        else:
            return left or right
            
            
            
            
def lowestCommonAncestor(self, root, p, q):
    def path(root, goal):
        path, stack = [], [root]
        while True:
            node = stack.pop()
            if node:
                if node not in path[-1:]:
                    path += node,
                    if node == goal:
                        return path
                    stack += node, node.right, node.left
                else:
                    path.pop()
    path1 = path(root, p)
    path2 = path(root, q)
    LCA = None
    for a, b in zip(path1, path2):
        if a==b:
            LCA = a
        else:
            break
    return LCA
        
