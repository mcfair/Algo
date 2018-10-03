class Solution(object):
    def inorderTraversal(self, root):
 
        def inorder(root):
            if root:
                for x in inorder(root.left): yield x
                yield root
                for x in inorder(root.right): yield x
            ##to display tree hierarchy, we can print null node as "#"
            #else:
            #    yield TreeNode("#")
        return [x.val for x in inorder(root)]
