
class RecursiveSolution(object):
    def postorder(self, root):
        if not root: return []
  
        res = []
        for kid in root.children:
            res += self.postorder(kid)
        res.append(root.val)
        
        return res
