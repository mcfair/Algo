
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """       
        if inorder:
            ind = inorder.index(postorder.pop())
            root = TreeNode(inorder[ind])
            #must build from right to left, as we pop root from the end of postorder list
            root.right = self.buildTree(inorder[ind+1:], postorder)
            root.left = self.buildTree(inorder[:ind], postorder)
            return root

