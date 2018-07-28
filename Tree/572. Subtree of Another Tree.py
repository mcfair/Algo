class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        sstr = ''
        for x in self.preorder(s):
            sstr += str(x.val)
        
        
        tstr = ''
        for x in self.preorder(t):
            tstr += str(x.val)
       
        return tstr in sstr
        
    def preorder(self, node):
        if node:
            yield TreeNode('#') #represent start of a subtree
            yield node
            for x in self.preorder(node.left): yield x
            for x in self.preorder(node.right): yield x
            yield TreeNode('*') #represent leaf end
    
