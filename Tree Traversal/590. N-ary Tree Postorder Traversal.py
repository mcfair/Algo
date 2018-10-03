
class RecursiveSolution(object):
    def postorder(self, root):
        if not root: return []
  
        res = []
        for kid in root.children:
            res += self.postorder(kid)
        res.append(root.val)
        
        return res
"""
almost impossible to do postorder directly
we first do "preorder", then reverse the result
"""
class IterativeSolution(object): 
    def postorder(self, root):
        if not root: return []
        stack = [root]
        res = []
        while stack:
            p=stack.pop()
            res.append(p.val)
            stack.extend(p.children)
        return reversed(res)
       
      #compare and contrast with preorder code
      def preorder(self, root):
        if not root: return []
        stack = [root]
        res = []
        while stack:
            p=stack.pop()
            res.append(p.val)
            stack.extend(p.children[::-1])
        return res
