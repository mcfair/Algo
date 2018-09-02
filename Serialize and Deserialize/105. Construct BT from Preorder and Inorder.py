
class Solution(object):
    def buildTree(self, preorder, inorder):
        if inorder:
            #first item in preorder list is the root
            ind = inorder.index(preorder.pop(0))
            #build the tree
            root = TreeNode(inorder[ind])
            root.left = self.buildTree(preorder, inorder[0:ind])
            root.right = self.buildTree(preorder, inorder[ind+1:])
            return root
