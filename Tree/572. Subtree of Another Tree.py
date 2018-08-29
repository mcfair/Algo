class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """ 
        if not s: return False
        def isSameTree(p, q):
            if not p and not q: return True
            if not p or not q: return False
            if p.val != q.val: return False
            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
        
        return isSameTree(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
        

#Use a helper function "check"
class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        
        if not s and not t:
            return True
        if not s or not t:
            return False
        
        if self.check(s,t):
            return True
        
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
 
    def check(self, s, t):
        if not s and not t:
            return True
        if not s or not t:
            return False        
        if s.val  != t.val:
            return False
        return self.check(s.left, t.left) and self.check(s.right, t.right)

#use preorder traversal to generate a string
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
    
